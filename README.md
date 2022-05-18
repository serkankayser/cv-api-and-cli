# CV API & CLI

CV API & CLI is a REST API and prints data from CV using CLI commands.

## Installation

Activate the environment.

```bash
source cv-venv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages from requirements.txt.

```bash
pip install -r requirements.txt
```

## Run the app

```bash
flask run
```

# Usage REST API
The REST API to the app is described below.

```bash
# Base url:
http://127.0.0.1:5000
```
```bash
# To get personal data from the CV:
http://127.0.0.1:5000/personal
```
```bash
# To get projects from the CV:
http://127.0.0.1:5000/projects
```
## Available Endpoints
`/all` To get all CV data.

`/education` To get education data from the CV.

`/experience` To get experience data from the CV.

`/languages` To get languages data from the CV.

`/personal` To get personal data from the CV.

`/personal_skills` To get personal skills from the CV.

`/projects` To get personal projects from the CV.

`/tech_skills` To get tech skills from the CV.

# Usage Flask CLI Commands
The CLI commands for the app is described below.
```bash
# Run this command to print personal data from the CV:
flask personal
```
```bash
# Run this command to print projects from the CV:
flask projects
```
## Available Commands
`flask --help` To see all available commands.

`flask routes` To see all available routes.

`flask all` To get all CV data.

`flask education` To get education data from the CV.

`flask experience` To get experience data from the CV.

`flask languages` To get languages data from the CV.

`flask personal` To get personal data from the CV.

`flask personal_skills` To get personal skills from the CV.

`flask projects` To get personal projects from the CV.

`flask tech_skills` To get tech skills from the CV.

Thank you.