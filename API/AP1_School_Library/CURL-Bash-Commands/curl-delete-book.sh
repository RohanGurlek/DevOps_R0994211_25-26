#!/bin/bash
APIKEY="cisco|fscmeh7DQsuVWHF2dTlwAjlYeMlnhp_ar8uJeXuVKC8"
BOOK=101
DELETE_URL="http://library.demo.local/api/v1/books/$BOOK"
echo $DELETE_URL
curl -X DELETE $DELETE_URL \
-H "accept: application/json" \
-H "X-API-KEY: $APIKEY" \
-H "Content-Type: application/json"
echo "cur date/time $(date)"
