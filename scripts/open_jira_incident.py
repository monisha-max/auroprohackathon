import os
import requests
from requests.auth import HTTPBasicAuth

jira_url = os.environ['JIRA_SITE']
jira_email = os.environ['JIRA_EMAIL']
jira_token = os.environ['JIRA_API_TOKEN']
project_key = os.environ['JIRA_PROJECT_KEY']
run_number = os.environ.get('GITHUB_RUN_NUMBER', 'unknown')

summary = f"Deployment Failure: Build {run_number}"
description = "Deployment failed. Please investigate."

data = {
    "fields": {
        "project": {"key": project_key},
        "summary": summary,
        "description": description,
        "issuetype": {"name": "Bug"}
    }
}

response = requests.post(
    f"{jira_url}/rest/api/2/issue",
    json=data,
    auth=HTTPBasicAuth(jira_email, jira_token),
    headers={"Content-Type": "application/json"}
)
print(response.status_code, response.text) 