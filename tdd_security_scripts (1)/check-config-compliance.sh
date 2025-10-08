#!/usr/bin/env bash
set -e
non_compliant=$(aws configservice describe-compliance-by-config-rule --query 'ComplianceByConfigRules[?Compliance.ComplianceType==`NON_COMPLIANT`].ConfigRuleName' --output text)
if [ -z "$non_compliant" ]; then
  echo "GREEN: Todas las reglas Config están en cumplimiento"
else
  echo "RED: Reglas NO cumplidas: $non_compliant"
  exit 1
fi
