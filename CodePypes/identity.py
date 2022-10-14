import json
from pickle import TRUE
from sqlite3 import paramstyle
import webbrowser
import requests
from .Organization import Organization

from .environment import auth_token
from .environment import api_url

def login():
    url = api_url("identity", "login")
    
    params = { "idpName": "google", 
          "clientRedirect": "http://localhost:52841" }

    sso = { "sso": params }

    x = requests.post(url, json=sso, allow_redirects=TRUE)

    response = x.json()
    print(response['redirectURL'])
    webbrowser.open(response['redirectURL'])

def logout():
    print("logout")

def organizations():
    url = api_url("identity", "organizations")
    x = requests.get(url, headers = { "Authorization": auth_token })
    return x.json()

def profile():
    url = api_url("identity", "users/self/profile")
    x = requests.get(url, headers = { "Authorization": auth_token })
    return x.json()
