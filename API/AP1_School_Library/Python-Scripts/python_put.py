import requests
import json
from faker import Faker


APIHOST = "http://library.demo.local"
LOGIN = "cisco"
PASSWORD = "Cisco123!"
def getAuthToken():
    authCreds = (LOGIN, PASSWORD)
    r = requests.post(
        f"{APIHOST}/api/v1/loginViaBasic", 
        auth = authCreds
    )
    if r.status_code == 200:
        return r.json()["token"]
    else:
        raise Exception(f"Status code {r.status_code} and text {r.text}, while trying to Auth.")
def putBook(id, book, apiKey):
    r = requests.put(
        f"{APIHOST}/api/v1/books/{id}",
        headers= {
            "Content-type": "application/json",
            "X-API-KEY": apiKey
        },
        data = json.dumps(book)
    )
    if r.status_code == 200:
        print(f"book {book} updated")
    else:
        raise Exception(f"Error code {r.status_code}")
    
apiKey = getAuthToken()
fake = Faker()
id = int(input("geef oude id: "))
book = {
    "id":int(input("geef ID: ")), 
    "title": input("geef titel: "), 
    "author": input("geef auteur: "), 
    "isbn": fake.isbn13()
    }

putBook(id, book, apiKey)