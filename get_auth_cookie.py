import requests
from urllib3.exceptions import InsecureRequestWarning
import urllib3
import sys

# For ignoring SSL warnings.
urllib3.disable_warnings(InsecureRequestWarning)

cp_api_endpoint = "https://clearpass_url.com/api/"

# configurable in /guest/api_clients.php
cp_api_key = "Clearpass_client_ID"
cp_api_secret = "Clearpass_client_Secret"

# Sending request to clearpass
auth = requests.post("{}/oauth".format(cp_api_endpoint), data={"grant_type": "client_credentials"}, verify=False, auth=(cp_api_key, cp_api_secret))
# Binding response to variable called access_token
access_token = auth.json()['access_token']


print(access_token)
