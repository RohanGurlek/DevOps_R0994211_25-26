# Fill in this file with the code to create a room membership from the Webex Teams exercise
# create-membership.py
# Add a user to a room

import requests
import json
from config import ACCESS_TOKEN

access_token = ACCESS_TOKEN
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vNTUyYzE4MjAtZmEzMS0xMWYwLWE2N2MtZDdiNjU4NjhjOGY3'
person_email = 'rohan.gurlek@student.odisee.be'

url = 'https://webexapis.com/v1/memberships'
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

payload = {
    'roomId': room_id,
    'personEmail': person_email
}

res = requests.post(url, headers=headers, json=payload)
print(json.dumps(res.json(), indent=4))
