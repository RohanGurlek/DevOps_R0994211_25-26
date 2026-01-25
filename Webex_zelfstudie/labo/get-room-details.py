# Fill in this file with the code to get room details from the Webex Teams exercise
# get-room-details.py
# Retrieve meeting details for a room

import requests
import json
from config import ACCESS_TOKEN

access_token = ACCESS_TOKEN
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vNTUyYzE4MjAtZmEzMS0xMWYwLWE2N2MtZDdiNjU4NjhjOGY3'

url = f'https://webexapis.com/v1/rooms/{room_id}/meetingInfo'
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
