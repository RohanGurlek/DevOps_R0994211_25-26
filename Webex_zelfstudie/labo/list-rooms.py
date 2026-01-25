# Fill in this file with the rooms/spaces listing code from the Webex Teams exercise
# list-rooms.py
# List all rooms for authenticated user

import requests
import json
from config import ACCESS_TOKEN

access_token = ACCESS_TOKEN

url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}
params = {'max': '100'}

res = requests.get(url, headers=headers, params=params)
print(json.dumps(res.json(), indent=4))
