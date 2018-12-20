#!/bin/bash

INTERVAL="${INTERVAL:-7200}"

while true; do
  echo "Running mreg..."
  mreg || echo "Something went wrong!"
  sleep "${INTERVAL}"
done