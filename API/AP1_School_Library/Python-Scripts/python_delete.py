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
    

def deleteBook(bookId, apiKey):
    r = requests.delete(
        f"{APIHOST}/api/v1/books/{bookId}",
        headers = {
            "Content-type" : "application/json",
            "X-API-KEY": apiKey
        }
    )
    if r.status_code == 200:
        print (f"book {bookId} deleted")
    else:
        print (r.status_code)

apiKey = getAuthToken()
id = int(input('welk boek wilt u verwijderen (id): '))

deleteBook(id, apiKey)
