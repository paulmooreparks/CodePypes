import json
from pickle import TRUE
from sqlite3 import paramstyle
import webbrowser
import requests
from .Organization import Organization

from .environment import auth_token
from .environment import endpoint

def login():
    url = "https://api.codepipes.io/identity/v0/login"
    
    params = { "idpName": "google", 
          "clientRedirect": "http://localhost:52841" }

    sso = { "sso": params }

    x = requests.post(url, json=sso, allow_redirects=TRUE)

    response = x.json()
    print(response['redirectURL'])
    webbrowser.open(response['redirectURL'])

def print_url(r, *args, **kwargs):
    print(r.url)

def logout():
    print("logout")

def organizations():
    url = "https://api.codepipes.io/identity/v0/organizations"
    print(url)      
    x = requests.get(url, headers = { "Authorization": auth_token })
    print(x.status_code)
    print(x.request.path_url)
    print(x.json())
