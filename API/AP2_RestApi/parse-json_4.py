import requests
import urllib.parse

route_url = "https://graphhopper.com/api/1/route?"
key = "b65baeb1-1636-4004-abca-5a533f33ef72"

def geocoding(location, key):
    while location == "":
        location = input("Enter the location again: ")

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
        value = json_data["hits"][0]["osm_value"]
        country = json_data["hits"][0].get("country", "")
        state = json_data["hits"][0].get("state", "")

        if state and country:
            new_loc = f"{name}, {state}, {country}"
        elif country:
            new_loc = f"{name}, {country}"
        else:
            new_loc = name

        print("Geocoding API URL for " + new_loc + " (Location Type: " + value + ")\n" + url)
    else:
        lat = "null"
        lng = "null"
        new_loc = location
        if json_status != 200:
            print("Geocode API status:", json_status)
            print("Error message:", json_data.get("message", ""))

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
