# Fill in this file with the code to create a new room from the Webex Teams exercise
# create-rooms.py
# Create a new Webex room

import requests
import json
from config import ACCESS_TOKEN

access_token = ACCESS_TOKEN

url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

payload = {'title': 'DevNet Associate Training!'}

res = requests.post(url, headers=headers, json=payload)
print(json.dumps(res.json(), indent=4))
