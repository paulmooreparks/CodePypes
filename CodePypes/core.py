import os
import requests
import webbrowser
import yaml
from pathlib import Path

endpoint = "api.codepipes.io"
auth_token = ""

home_directory = os.path.expanduser( '~' )
cp_state_file = ".codepipes_state.yaml"
cp_state_path_fmt = "{home}/{file}"
cp_state_path = cp_state_path_fmt.format(home=home_directory,file=cp_state_file)

config = yaml.safe_load(Path(cp_state_path).read_text())
endpoint = config['connected_endpoint']
auth_token = config['auth_token']
version = "v0"

endpoint_fmt = "https://{endpoint}"
endpoint_url = endpoint_fmt.format(endpoint=endpoint)
api_fmt = "{url}/{api}/{version}/{method}"

def login():
    url = api_url("identity", "login")
    
    params = { "idpName": "google", "clientRedirect": "http://localhost:52841" }

    sso = { "sso": params }

    x = requests.post(url, json=sso, allow_redirects=TRUE)

    rsp = x.json()
    webbrowser.open(rsp['redirectURL'])
    rsp.close()

def logout():
    print("logout")

def api_url(api, method):
    return api_fmt.format(url=endpoint_url, version=version, api=api, method=method)

def get_api(api, method):
    url = api_url(api, method)
    rsp = requests.get(url, headers = { "Authorization": auth_token })
    json = { "status_code": rsp.status_code, "response": rsp.json() }
    rsp.close()
    return json

def make_dict(collection, key):
    items = {}
    for item in collection:
        items[item[key]] = item

    return items

