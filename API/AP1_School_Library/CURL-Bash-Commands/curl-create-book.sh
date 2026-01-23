#!/bin/bash
APIKEY="cisco|7EJPISYa3M1CguJ9c4qNt6Qr63SO-bDyNHUUjF_fDcU"
BOOK_ID=202
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