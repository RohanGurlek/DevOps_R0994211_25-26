# Fill in this file with the people listing code from the Webex Teams exercise
# list-people.py
# List people by email and fetch details by person ID

import requests
import json
from config import ACCESS_TOKEN

access_token = ACCESS_TOKEN
email = 'rohan.gurlek@student.odisee.be'
person_id = 'PERSON_ID_HERE'

headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

# List people
url = 'https://webexapis.com/v1/people'
params = {'email': email}
res = requests.get(url, headers=headers, params=params)
print(json.dumps(res.json(), indent=4))

# Get person details
url = f'https://webexapis.com/v1/people/{person_id}'
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
