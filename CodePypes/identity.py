import json

from .core import auth_token
from .core import get_api

def get_profile():
    return get_api("identity", "users/self/profile")

def get_organizations():
    return get_api("identity", "organizations")

def get_organizations_by_name():
    org_dict = {}
    orgs = organizations()

    if orgs['status_code'] == 200:
        for org in orgs['response']['orgs']:
            org_dict[org['name']] = org

    return org_dict

def get_organization_by_name(name):
    orgs = get_organizations_by_name()
    return orgs[name]

def get_organizations_by_id():
    org_dict = {}
    orgs = organizations()

    if orgs['status_code'] == 200:
        for org in orgs['response']['orgs']:
            org_dict[org['id']] = org

    return org_dict

def get_organization_by_id(id):
    orgs = get_organizations_by_id()
    return orgs[id]

