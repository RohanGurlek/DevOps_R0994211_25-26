#!/bin/bash
APIKEY="cisco|H4gw2oBNr85O3Rur5m5d5y-3jEFe1O3UaEcqJ_VeGkI"
BOOK=3
NEW_BOOK_ID=3
NEW_BOOK_TITLE="boekje is leuk"
NEW_BOOK_AUTHOR="piet pieters"
UPDATE_URL="http://library.demo.local/api/v1/books/$BOOK"
echo $UPDATE_URL
curl -X PUT $UPDATE_URL \
-H "accept: application/json" \
-H "X-API-KEY: $APIKEY" \
-H "Content-Type: application/json" \
-d "{\"id\": $NEW_BOOK_ID, \"title\": \"$NEW_BOOK_TITLE\", \"author\": \"$NEW_BOOK_AUTHOR\"}"
echo "cur date/time $(date)"