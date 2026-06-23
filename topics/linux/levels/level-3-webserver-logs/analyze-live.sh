#!/usr/bin/env bash

if [ $# -lt 1 ]; then
    echo "Usage: ./analyze-live.sh <logfile> [N]"
    exit 1
fi

LOGFILE=$1
TOPN=${2:-5}

if [ ! -f "$LOGFILE" ]; then
    echo "Error: File '$LOGFILE' not found"
    exit 1
fi

echo "=== Top $TOPN IPs ==="
awk '{print $1}' "$LOGFILE" | sort | uniq -c | sort -rn | head -n "$TOPN"

echo
echo "=== Errors ==="
echo "4xx errors: $(awk '$9 ~ /^4[0-9][0-9]$/ {c++} END {print c+0}' "$LOGFILE")"
echo "5xx errors: $(awk '$9 ~ /^5[0-9][0-9]$/ {c++} END {print c+0}' "$LOGFILE")"

echo
echo "=== Busiest hour ==="
awk -F'[:[]' '{print $4}' "$LOGFILE" | sort | uniq -c | sort -rn | head -1 | awk '{print $2":00 (count: "$1")"}'

echo
echo "=== Total ==="
echo "Total requests processed: $(wc -l < "$LOGFILE")"
