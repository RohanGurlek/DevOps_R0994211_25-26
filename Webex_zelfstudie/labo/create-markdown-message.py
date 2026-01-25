# Fill in this file with the messages code from the Webex Teams exercise
# create-markdown-message.py
# Send a markdown message to a room

import requests
import json
from config import ACCESS_TOKEN

access_token = ACCESS_TOKEN
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vNTUyYzE4MjAtZmEzMS0xMWYwLWE2N2MtZDdiNjU4NjhjOGY3'
message = 'Hello **DevNet Associates**!!'

url = 'https://webexapis.com/v1/messages'
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

payload = {
    'roomId': room_id,
    'markdown': message
}

res = requests.post(url, headers=headers, json=payload)
print(json.dumps(res.json(), indent=4))
