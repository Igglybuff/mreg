#!/bin/bash

INTERVAL="${INTERVAL:-7200}"

while true; do
  sleep "${INTERVAL}"
  mreg
done