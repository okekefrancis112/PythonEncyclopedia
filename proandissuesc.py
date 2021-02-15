from requests.auth import HTTPBasicAuth 
import json
import requests

def get_project(domain_name,auth,headers, project_key):
    url = f"https://{domain_name}.atlassian.net/rest/api/latest/project/{project_key}"
    response = requests.request("GET", url, headers=headers, auth=auth)
    log = json.loads(response.text)
    name = log["name"]
    id = log["id"]
    key = log["key"]
    print(f"Project Name=>", name)
    print(f"Project Id=>", id)
    print(f"Project Key=>", key)

def get_issue(domain_name,auth, headers, project_key):
    url = f"https://{domain_name}.atlassian.net/rest/api/3/search?jql=project={project_key}"
    response = requests.request("GET", url, headers=headers, auth=auth)
    log = json.loads(response.text)
    res = log["issues"]
    for i, item in enumerate(res): 
        id = (item["id"])
        key =(item["key"])
        opt = (id, key)
        data = ('"ID":"%s","KEY":"%s"') %(id, key)
        print(data)