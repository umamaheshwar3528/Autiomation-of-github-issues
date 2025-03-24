# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://umreddy23.atlassian.net/rest/api/3/issue"

auth = HTTPBasicAuth("umreddy23@gmail.com", "ATATT3xFfGF0rsS-h2aprsf6Y6Y2dvu2Hj8r16P7jcQqwfN3rUttisfmcsV0Rk7gMj2bPSrk-JXvXAVxJkrZQmNKk6vqIGILQyNyfqv3pRsyNqDVpsj1saWgMdJsem5d8A24wcn8ZaGRBNlmmCczMCrsn9Wjfsx6SqIN0HpY3oSVCeiCuefON3Y=F5B1879A")

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first Jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "issuetype": {
      "id": "10001"
    },
    "project": {
      "key": "MFLP"
    },
    "summary": "First Jira ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))