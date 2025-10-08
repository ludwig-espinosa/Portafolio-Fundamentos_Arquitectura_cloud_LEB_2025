#!/usr/bin/env bash
# Simula ataque SQLi contra el endpoint público y verifica WAF logs
URL=$1
if [ -z "$URL" ]; then
  echo "Uso: $0 <url>"
  exit 1
fi
echo "Lanzando ataque SQLi simulado contra $URL"
curl -s -o /dev/null -w "%{http_code}\n" -X GET "$URL?user=1' OR '1'='1"
echo "Revisar AWS WAF logs en CloudWatch para confirmar bloqueo."
