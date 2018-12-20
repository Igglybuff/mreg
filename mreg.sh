#!/bin/bash

URL="https://www.dvdsreleasedates.com/"

MATCH_EXPRESSION=$(lynx -dump "${URL}" | \
  grep -i "Most Requested DVD Release Dates" -A 15 | \
  grep -i -v "Most Requested DVD Release Dates" | \
  tr '.' '\n' | \
  sed -e 's/[0-9]*//g' -e 's/\[//g' \
  -e 's/\]//g' -e '/^[[:space:]]*$/d' \
  -e 's/\///g' -e 's/^[[:space:]]*//' \
  -e 's/[[:space:]]*$//' -e 's/$/\*/' | \
  tr '\n' ',' | \
  tr ' ' '?')

echo ${MATCH_EXPRESSION::-1}