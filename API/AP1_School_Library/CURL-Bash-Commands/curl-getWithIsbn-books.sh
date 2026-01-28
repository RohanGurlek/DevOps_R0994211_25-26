#!/bin/bash
APIKEY="cisco|H4gw2oBNr85O3Rur5m5d5y-3jEFe1O3UaEcqJ_VeGkI"
Get_WithISBN_URL="http://library.demo.local/api/v1/books?includeISBN=true"
echo $Get_WithISBN_URL
curl -X GET $Get_WithISBN_URL \
-H "accept: application/json"
echo "cur date/time $(date)"
