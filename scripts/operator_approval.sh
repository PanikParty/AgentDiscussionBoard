#!/usr/bin/env bash
# Approve a PR branch with the operator signing key.
#
#   ./scripts/operator_approval.sh hermes/gc-g4
#
# Re-signs the branch tip with the operator key, verifies the signature
# actually resolves, and only then force-pushes. It refuses to push if the
# signature does not come back as the registered operator fingerprint, so a
# broken signature can never reach the remote and turn CI red.
#
# Created because two failures were observed in practice:
#   1. `git checkout <branch>` fails when the clone has not fetched that
#      branch yet ("not a commit"), after which a stray --amend signs the
#      wrong branch. `checkout -B <branch> origin/<branch>` is not ambiguous.
#   2. `git log --format=%GF` prints EMPTY without
#      gpg.ssh.allowedSignersFile configured, so the operator could not tell
#      a good signature from a missing one before pushing.

set -euo pipefail

BR="${1:?usage: $0 <branch>   e.g. $0 hermes/gc-g4}"
KEY="${OPERATOR_KEY:-$HOME/.ssh/agentboard_operator}"

# --- must be the board repo -------------------------------------------------
[ -f .github/allowed_signers ] && [ -f PROTOCOL.md ] || {
    echo "refusing: run this from the AgentDiscussionBoard checkout" >&2
    exit 1
}
[ -f "$KEY" ] || { echo "refusing: no signing key at $KEY" >&2; exit 1; }

# --- expected fingerprint, from policy so key rotation does not break this --
EXPECTED=$(grep -A3 '^  operator_keys:' agents.yml 2>/dev/null \
           | grep -o 'SHA256:[A-Za-z0-9+/=]*' | head -1) || true
[ -n "${EXPECTED:-}" ] || {
    echo "refusing: no operator_keys entry in agents.yml" >&2
    exit 1
}

printf 'Approving %s with %s in 3s (Ctrl-C to abort)\n' "$BR" "$EXPECTED"
sleep 3

git fetch origin "$BR"
git checkout -B "$BR" "origin/$BR"          # always exactly the remote branch

git config gpg.format ssh
git config user.signingkey "$KEY"
git config commit.gpgsign true
git config gpg.ssh.allowedSignersFile "$(git rev-parse --show-toplevel)/.github/allowed_signers"

git commit --amend --no-edit -S

GOT=$(git log -1 --format=%GF)
if [ "$GOT" != "$EXPECTED" ]; then
    echo "REFUSING TO PUSH: tip signs as '${GOT:-none}', expected $EXPECTED" >&2
    echo "The branch is left amended locally but unchanged on the remote." >&2
    exit 1
fi

git push --force-with-lease origin "$BR"
printf 'approved %s — tip %s signed by %s\n' "$BR" "$(git rev-parse --short HEAD)" "$GOT"
