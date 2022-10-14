import json

from .core import auth_token
from .core import get_api
from .core import make_dict

def get_profile(id):
    return get_api("identity", "users/{id}/profile".format(id=id))

def get_self():
    return get_api("identity", "users/self/profile")

def get_organizations():
    return get_api("identity", "organizations")

def get_organizations_by_name():
    orgs = {}
    rsp = get_organizations()

    if rsp['status_code'] == 200:
        orgs = make_dict(rsp['response']['orgs'], 'name')

    return orgs

def get_organization_by_name(name):
    orgs = get_organizations_by_name()
    return orgs[name]

def get_organizations_by_id():
    orgs = {}
    rsp = get_organizations()

    if rsp['status_code'] == 200:
        orgs = make_dict(rsp['response']['orgs'], 'id')

    return orgs

def get_organization_by_id(id):
    orgs = get_organizations_by_id()
    return orgs[id]

def get_credentials(organization_id):
    return get_api("identity", "organizations/{id}/creds".format(id=organization_id))

def get_projects(organization_id):
    return get_api("identity", "organizations/{id}/projects".format(id=organization_id))

def get_projects_by_name(organization_id):
    projects = {}
    rsp = get_projects(organization_id)

    if rsp['status_code'] == 200:
        projects = make_dict(rsp['response']['projs'], 'name')

    return projects

def get_project_by_name(organization_id, name):
    projects = get_projects_by_name(organization_id)
    return projects[name]

