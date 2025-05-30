import os
import requests
import json
TOKEN = os.getenv("GH_TOKEN")
OWNER = "actions"
REPO = "setup-python"
ISSUE_NUMBER = 1101
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}
url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues/{ISSUE_NUMBER}"
response = requests.get(url, headers=headers)
issue_data = response.json()
print(json.dumps(issue_data, indent=2))