# Fill in this file with the membership code from the Webex Teams exercise
# list-memberships.py
# List room memberships

import requests
import json
from config import ACCESS_TOKEN

access_token = ACCESS_TOKEN
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vNTUyYzE4MjAtZmEzMS0xMWYwLWE2N2MtZDdiNjU4NjhjOGY3'

url = 'https://webexapis.com/v1/memberships'
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}
params = {'roomId': room_id}

res = requests.get(url, headers=headers, params=params)
print(json.dumps(res.json(), indent=4))
