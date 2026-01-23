import requests
import json
import datetime

APIHOST = "http://library.demo.local"
LOGIN = "cisco"
PASSWORD = "Cisco123!"

def getBookById(id):
    r = requests.get(
        f"{APIHOST}/api/v1/books/{id}",
        headers={
            "content-type": "application/json"
        }
    )
    if r.status_code == 200:
        print(json.dumps(r.json(), indent=4))
    else:
        print("Error:", r.status_code)

getBookById(int(input("geef boek id: ")))
date = datetime.now()
print(date)
