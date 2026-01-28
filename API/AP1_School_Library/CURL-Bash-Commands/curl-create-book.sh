#!/bin/bash
APIKEY="cisco|H4gw2oBNr85O3Rur5m5d5y-3jEFe1O3UaEcqJ_VeGkI"
BOOK_ID=101
BOOK_TITLE="Demo POST boek"
BOOK_AUTHOR="Demo auteur"
POST_URL="http://library.demo.local/api/v1/books"
echo $POST_URL
curl -X POST $POST_URL \
-H "accept: application/json" \
-H "X-API-KEY: $APIKEY" \
-H "Content-Type: application/json" \
-d "{ \"id\": $BOOK_ID, \"title\": \"$BOOK_TITLE\", \"author\": \"$BOOK_AUTHOR\"}"
echo "cur date/time $(date)"