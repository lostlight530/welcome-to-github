#!/bin/bash
# Robust Portal Verification Script
# Inspired by AI Agent collective intelligence

set -e

REPO_PATH=${1:-"."}

echo "🔍 Starting Portal Verification..."

# Check for essential files
files=("index.html" "src/scripts/translations.js" "README.md")
for file in "${files[@]}"; do
    if [ ! -f "$REPO_PATH/$file" ]; then
        echo "❌ Error: $file not found!"
        exit 1
    fi
done

# Check for branding consistency
if ! grep -q "lostlight-portal" "$REPO_PATH/README.md"; then
    echo "⚠️ Warning: lostlight-portal not found in README.md"
fi

# Check for valid HTML structure
if ! grep -i -q "<!DOCTYPE html>" "$REPO_PATH/index.html"; then
    echo "❌ Error: Invalid HTML structure in index.html"
    exit 1
fi

# Check for JS Syntax errors in index.html (Simple check for duplicate declarations)
# This is a bit naive but would have caught the previous error
if grep -q "let currentLang" "$REPO_PATH/index.html" && [ $(grep -c "let currentLang" "$REPO_PATH/index.html") -gt 1 ]; then
    echo "❌ Error: Duplicate JavaScript declarations found in index.html!"
    exit 1
fi

echo "✅ Portal Verification Passed!"
