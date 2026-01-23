import requests
import urllib.parse

route_url = "https://graphhopper.com/api/1/route?"
key = "b65baeb1-1636-4004-abca-5a533f33ef72"

def geocoding(location, key):
    geocode_url = "https://graphhopper.com/api/1/geocode?"
    url = geocode_url + urllib.parse.urlencode({
        "q": location,
        "limit": "1",
        "key": key
    })
    replydata = requests.get(url)
    json_data = replydata.json()
    json_status = replydata.status_code

    if json_status == 200 and len(json_data["hits"]) != 0:
        lat = json_data["hits"][0]["point"]["lat"]
        lng = json_data["hits"][0]["point"]["lng"]
        name = json_data["hits"][0]["name"]
        country = json_data["hits"][0].get("country", "")
        state = json_data["hits"][0].get("state", "")
        new_loc = ", ".join(filter(None, [name, state, country]))
    else:
        lat = "null"
        lng = "null"
        new_loc = location

    return json_status, lat, lng, new_loc

while True:
    loc1 = input("Starting Location: ")
    if loc1 in ("q", "quit"):
        break
    orig = geocoding(loc1, key)

    loc2 = input("Destination: ")
    if loc2 in ("q", "quit"):
        break
    dest = geocoding(loc2, key)

    print("=================================================")
    if orig[0] == 200 and dest[0] == 200:
        op = "&point=" + str(orig[1]) + "%2C" + str(orig[2])
        dp = "&point=" + str(dest[1]) + "%2C" + str(dest[2])

        paths_url = route_url + urllib.parse.urlencode({"key": key}) + op + dp
        paths_status = requests.get(paths_url).status_code
        paths_data = requests.get(paths_url).json()

        print("Routing API Status:", paths_status)
        print("Routing API URL:\n" + paths_url)
