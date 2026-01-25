# Fill in this file with the authentication code from the Webex Teams exercise
# authentication.py
# Test Webex access token

import requests
import json
from config import ACCESS_TOKEN

access_token = ACCESS_TOKEN

url = 'https://webexapis.com/v1/people/me'
headers = {
    'Authorization': f'Bearer {access_token}'
}

response = requests.get(url, headers=headers)
print(json.dumps(response.json(), indent=4))
