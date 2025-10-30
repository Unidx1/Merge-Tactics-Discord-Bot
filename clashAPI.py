import requests
from pprint import pprint
from dotenv import load_dotenv
import os
load_dotenv()

JWT_TOKEN = os.getenv("JWT")

BASE_URL = os.getenv("BASE_API_URL")


headers = {
    "Authorization": f"Bearer {JWT_TOKEN}"}

def getPlayerData(tag: str):
    url = BASE_URL + "/players/"
    tag = tag.replace("#", "%23").upper()
    print(BASE_URL + tag)
    try:
        response = requests.get(url= url + tag, headers= headers, timeout= 15)
        pprint(response.json()["progress"]["AutoChess_2025_Nov"])
        print(f"Status Code: {response.status_code}")
        return response.json()
    except:
        print(f"Status Code: {response.status_code}")
        print("An error has occured")
        pprint(response.json())
        return response

def getTop10k():
    url = BASE_URL + "/leaderboard/170000012?limit=1&after=eyJwb3MiOjk5OTl9"
    try:
        response = requests.get(url= url, headers= headers, timeout= 15)
        pprint(response.json())
        print(f"Status Code: {response.status_code}")
        return response.json()
    except:
        print(f"Status Code: {response.status_code}")
        print("An error has occured")
        pprint(response.json())
        return response

def getDoublesData(tag: str):
    tag = tag.replace("#", "%23").upper()
    url = BASE_URL + "/players/" + tag


#eyJwb3MiOjEwMDB9 <-- after no.1000
#eyJwb3MiOjUwMDB9 <-- after no.5000
#eyJwb3MiOjk5OTl9 <--- after no.9999 (do after to get 10,000)
#170000012 <-- Merge Tactics Leaderboard ID