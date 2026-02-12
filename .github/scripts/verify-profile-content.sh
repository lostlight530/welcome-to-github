#!/usr/bin/env bash

# This script verifies that PROFILE.md contains the expected welcome message
# and that the latest commit message is correct.

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <repository_path>"
    exit 1
fi

REPOSITORY_PATH=$1

cd "$REPOSITORY_PATH" || { echo "Directory $REPOSITORY_PATH not found"; exit 1; }

if [ ! -f PROFILE.md ]; then
  echo "PROFILE.md is missing" >&2
  exit 1
fi

if [ ! -s PROFILE.md ]; then
  echo "PROFILE.md is empty" >&2
  exit 1
fi

if ! grep -q "Welcome to my GitHub profile!" PROFILE.md; then
  echo "PROFILE.md should include the welcome message from the instructions" >&2
  exit 1
fi

latest_message=$(git log -1 --pretty=%B | head -n1)
if [ "$latest_message" != "Add PROFILE.md" ]; then
  echo "Latest commit message should be 'Add PROFILE.md' to match the instructions" >&2
  exit 1
fi
