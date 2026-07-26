# Jira Automation with Python

## Overview

This project demonstrates how to automate Jira Cloud using Python and the official Jira Python library.

The application securely authenticates with Jira using environment variables and creates a new Jira issue through the Jira REST API.

---

## Features

- Connect to Jira Cloud
- Secure authentication using API Token
- Create Jira issues programmatically
- Store credentials securely using a `.env` file
- Easy to extend for issue updates, comments, and searches

---

## Technologies Used

- Python 3
- Jira Python Library
- Jira REST API
- python-dotenv
- Git
- GitHub

---

## Project Structure

```
jira_demo.py
README.md
requirements.txt
.gitignore
.env (not uploaded to GitHub)
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/huzaifaabbasi23/selenium_project.git
```

### Move into the project directory

```bash
cd selenium_project
```

### Install the required packages

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project directory.

```
JIRA_EMAIL=your_email@example.com
JIRA_API_TOKEN=your_api_token
```

> **Note:** Never upload your `.env` file or API token to GitHub.

---

## How It Works

The application performs the following steps:

1. Loads credentials from the `.env` file.
2. Connects to Jira Cloud.
3. Authenticates using the Jira API Token.
4. Creates a new Task in the `SCRUM` project.
5. Prints the newly created issue key.

---

## Example Code

```python
issue_dict = {
    "project": {"key": "SCRUM"},
    "summary": "Account Locked",
    "description": "Account got locked",
    "issuetype": {"name": "Task"}
}

new_issue = jira.create_issue(fields=issue_dict)

print(new_issue.key)
```

---

## Sample Output

```
SCRUM-7
```

---

## Future Improvements

- Read Jira Issues
- Update Existing Issues
- Delete Issues
- Add Comments
- Read Comments
- Search Issues using JQL
- Attach files to Jira issues
- Handle exceptions and API errors

---

## Author

**Huzaifa Abbasi**

GitHub: https://github.com/huzaifaabbasi23