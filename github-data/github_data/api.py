import requests
import json

def get_data(username):
    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)
    if response.status_code == 200:
        raw_data = response.json()
        return raw_data
    else:
        print(f"Unable to retrive data {response.status_code}")

