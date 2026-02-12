#!/bin/bash

# Exit on any error
set -e

README_FILE="README.md"

echo "Checking if $README_FILE exists..."
if [ ! -f "$README_FILE" ]; then
    echo "Error: $README_FILE does not exist."
    exit 1
fi

echo "Checking for expected header in $README_FILE..."

# Check for the Octodex image
if ! grep -q "https://octodex.github.com/images/welcometocat.png" "$README_FILE"; then
    echo "Error: $README_FILE is missing the expected Octodex image."
    exit 1
fi

# Check for the Congratulations message
if ! grep -qi "Congratulations" "$README_FILE"; then
    echo "Error: $README_FILE is missing the expected Congratulations message."
    exit 1
fi

echo "Success: $README_FILE exists and contains the expected header."
