import requests

def fetchNo():
    noMessage = requests.get("https://naas.isalman.dev/no").json()
    if noMessage.status_code == 200:
        data = noMessage.json()
        print(f"Name: {data['name']}, Height: {data['height']}")
    else:
        print(f"Request failed with status code: {noMessage.status_code}")