from dotenv import load_dotenv
import os
from jira import JIRA
load_dotenv()

user = os.getenv("JIRA_EMAIL")
apikey =  os.getenv("JIRA_API_TOKEN")
server = "https://alnafia.atlassian.net"
ticket = "SCRUM-6"
jira = JIRA (server,basic_auth=(user,apikey))
issue = jira.issue(ticket)
comments= issue.fields.comment.comments
for comment in comments:
    print("My comment is :", comment.body)
    print("Comment Author is :", comment.author.displayName)
    print("Comment time is : ", comment.created)
    print("-----------------------------------------")