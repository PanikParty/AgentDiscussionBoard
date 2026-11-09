#!/bin/bash

echo "Approving branch $1 in 3 seconds"
sleep 1
echo "2.."
sleep 1
echo "1.."
sleep 1
echo "GO!"

set -x
git fetch origin $1
git checkout $1
git config gpg.format ssh && git config user.signingkey ~/.ssh/agentboard_operator && git config commit.gpgsign true
git commit --amend --no-edit -S
git push -f origin $1
