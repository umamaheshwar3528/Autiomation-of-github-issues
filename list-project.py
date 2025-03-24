
# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://umreddy23.atlassian.net/rest/api/3/project"

auth = HTTPBasicAuth("umreddy23@gmail.com", "ATATT3xFfGF0rsS-h2aprsf6Y6Y2dvu2Hj8r16P7jcQqwfN3rUttisfmcsV0Rk7gMj2bPSrk-JXvXAVxJkrZQmNKk6vqIGILQyNyfqv3pRsyNqDVpsj1saWgMdJsem5d8A24wcn8ZaGRBNlmmCczMCrsn9Wjfsx6SqIN0HpY3oSVCeiCuefON3Y=F5B1879A")

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

name = output[0]['name']

print(name)