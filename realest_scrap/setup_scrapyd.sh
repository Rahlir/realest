#!/bin/sh

REALEST_SCRAP_VERSION="0.1.0"
REALEST_SCRAP_URL="http://localhost:6800"

scrapyd&

SCRAPYD_PID=$!

N_CHECKS=0

while ! curl "$REALEST_SCRAP_URL"/daemonstatus.json; do
    if [ $N_CHECKS -gt 5 ]; then
        echo "Cannot connect to scrapyd"
        exit 1
    fi
    sleep 0.5 && ((N_CHECKS++))
done

scrapyd-deploy && kill "$SCRAPYD_PID" && exec "$@"
