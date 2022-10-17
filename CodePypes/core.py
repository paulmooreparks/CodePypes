import os
import requests
import webbrowser
import yaml
from pathlib import Path

endpoint = "api.codepipes.io"

home_directory = os.path.expanduser( '~' )
cp_state_file = ".codepipes_state.yaml"
cp_state_path_fmt = "{home}/{file}"
cp_state_path = cp_state_path_fmt.format(home=home_directory,file=cp_state_file)

def read_config():
    retval = yaml.safe_load(Path(cp_state_path).read_text())
    return retval

def write_config():
    with open(cp_state_path, 'w') as outfile:
        yaml.dump(config, outfile, default_flow_style=False)

config = read_config()
endpoint = config['connected_endpoint']
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
    rsp = requests.get(url, headers = { "Authorization": config['auth_token'] })
    json = { "status_code": rsp.status_code, "response": rsp.json() }
    rsp.close()
    return json

def post_api(api, method, body):
    url = api_url(api, method)
    rsp = requests.post(url, headers = { "Authorization": config['auth_token'] }, data = body)
    json = { "status_code": rsp.status_code, "response": rsp.json() }
    rsp.close()
    return json

def make_dict(collection, key):
    items = {}
    for item in collection:
        items[item[key]] = item

    return items

