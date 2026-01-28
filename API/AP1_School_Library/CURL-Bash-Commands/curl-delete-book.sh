#!/bin/bash
APIKEY="cisco|H4gw2oBNr85O3Rur5m5d5y-3jEFe1O3UaEcqJ_VeGkI"
BOOK=101
DELETE_URL="http://library.demo.local/api/v1/books/$BOOK"
echo $DELETE_URL
curl -X DELETE $DELETE_URL \
-H "accept: application/json" \
-H "X-API-KEY: $APIKEY" \
-H "Content-Type: application/json"
echo "cur date/time $(date)"
