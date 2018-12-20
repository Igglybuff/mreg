#!/bin/bash

set -euo pipefail

INTERVAL="${INTERVAL:-7200}"

if [ -z "${MREG_FILTER_NAME}" ]; then
  echo "ERROR - you have not specified a filter name!"
  exit 1
fi

while true; do
  echo "Running mreg..."
  mreg || echo "Something went wrong!"
  sleep "${INTERVAL}"
done