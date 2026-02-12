#!/usr/bin/env bash

# Checks to perform
checks='{
  "pr_title": {
    "name": "Pull request title",
    "passed": true,
    "message": ""
  },
  "pr_description": {
    "name": "Pull request description",
    "passed": true,
    "message": ""
  }
}'

# Check pull request title
if [ "$PR_TITLE" != "Add my first file" ]; then
  checks=$(echo $checks | jq '.pr_title.passed = false')
  checks=$(echo $checks | jq '.pr_title.message = "Incorrect title"')
fi

# Check if a pull request description exists
if [ "$PR_BODY" == "" ]; then
  checks=$(echo $checks | jq '.pr_description.passed = false')
  checks=$(echo $checks | jq '.pr_description.message = "Empty pull request description"')
fi

# Verify all checks passed
passed=$(echo $checks | jq '. | all(.passed?)')

# Flatten to an array for returning. Allows iteration during rendering.
results=$(echo $checks | jq 'to_entries | map({name: .key} + .value)')

# Save pass status to output
echo "passed=$passed" >> "$GITHUB_OUTPUT"

# Save results to output
echo 'results<<EOF' >> "$GITHUB_OUTPUT"
echo "$results" >> "$GITHUB_OUTPUT"
echo 'EOF' >> "$GITHUB_OUTPUT"
