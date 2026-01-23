#!/bin/bash
APIKEY="cisco|fscmeh7DQsuVWHF2dTlwAjlYeMlnhp_ar8uJeXuVKC8"
Get_WithISBN_URL="http://library.demo.local/api/v1/books?includeISBN=true"
echo $Get_WithISBN_URL
curl -X GET $Get_WithISBN_URL \
-H "accept: application/json"
echo "cur date/time $(date)"
