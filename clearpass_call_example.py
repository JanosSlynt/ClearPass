import requests
from urllib3.exceptions import InsecureRequestWarning
import urllib3
import sys
import json

urllib3.disable_warnings(InsecureRequestWarning)

cp_api_endpoint = "https://clearpass_url.com/api/"
#Input the cookie from get_auth_cookie.py
cp_cookie = sys.argv[1]

#!NOTE! authentication is done by specifying the Authorization header key and bearer cookie value.
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": 'Bearer {}'.format(cp_cookie)
}

data = {
    'mac' : 'AA-09-78-56-34-12',
    'description' : 'New device via API'
}

# data needs to be formatted to json by using json.dumps()
response = requests.post("{}/device".format(cp_api_endpoint), headers=headers, data = json.dumps(data), verify=False)


print(response.content)
print(response.status_code)
