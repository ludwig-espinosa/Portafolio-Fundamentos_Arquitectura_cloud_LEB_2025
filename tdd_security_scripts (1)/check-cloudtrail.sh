#!/usr/bin/env bash
set -e
trails=$(aws cloudtrail describe-trails --query 'trailList[?IsMultiRegionTrail==`true`].Name' --output text)
if [ -z "$trails" ]; then
  echo "RED: No existe CloudTrail multi-region"
  exit 1
else
  echo "GREEN: CloudTrail multi-region: $trails"
  exit 0
fi
