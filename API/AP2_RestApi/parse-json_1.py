import requests
import urllib.parse

geocode_url = "https://graphhopper.com/api/1/geocode?"
route_url = "https://graphhopper.com/api/1/route?"

loc1 = "Washington, D.C."
loc2 = "Baltimore, Maryland"
key = "b65baeb1-1636-4004-abca-5a533f33ef72"

url = geocode_url + urllib.parse.urlencode({
    "q": loc1,
    "limit": "1",
    "key": key
})

replydata = requests.get(url)
json_data = replydata.json()
json_status = replydata.status_code

print(json_data)
