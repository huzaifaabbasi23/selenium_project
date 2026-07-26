from jira import JIRA
from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv("JIRA_EMAIL")
apikey = os.getenv("JIRA_API_TOKEN")

server = "https://alnafia.atlassian.net"

jira = JIRA(server, basic_auth=(user, apikey))

issue_dict = {
    "project": {"key": "SCRUM"},
    "summary": "Account Locked",
    "description": "Account got locked",
    "issuetype": {"name": "Task"}
}

new_issue = jira.create_issue(fields=issue_dict)

print(f"Issue created successfully: {new_issue.key}")