# GitHub Data CLI
https://roadmap.sh/projects/github-user-activity

A simple **Python CLI tool** built with **Click** that fetches public GitHub user data using the GitHub API.

## Features

* Fetch GitHub user information from the terminal
* Simple command: `github-data <username>`
* Built with Click
* Editable install for development

 

## Project Structure

github-data/
├── github_data/
│   ├── __init__.py
│   ├── api.py
│   └── cli.py
├── pyproject.toml
└── README.md


 

## Requirements

* Python **3.8+**
* `pip`
* Internet connection (GitHub API)

 

## Setup Instructions

### 1. Clone or download the project

```bash
git clone <your-repo-url>
cd github-data
```

 

### 2. Create and activate virtual environment (recommended)

```bash
python3 -m venv .env
source .env/bin/activate
```

 

### 3. Install dependencies and CLI (editable mode)

```bash
pip install -e .
```

This registers the `github-data` command system-wide inside the virtual environment.

 

## Usage

### Basic command

```bash
github-data <github_username>
```

### Example

```bash
github-data torvalds
```

### Sample Output

```
Username  : torvalds
Name      : Linus Torvalds
Repos     : 6
Followers : 200000+
Following : 0
```

## Help

```bash
github-data --help
```

 

## Development Notes

* Editable install (`pip install -e .`) means:

  * No reinstall needed after code changes
  * Changes take effect immediately
* CLI entry point is defined in `pyproject.toml`

 

## Common Errors

### Command not found

Make sure:

* Virtual environment is activated
* You ran `pip install -e .` from the project root

### Module not found

Verify:

* Folder name is `github_data` (not `github-data`)
* `__init__.py` exists

 

## Technologies Used

* Python
* Click
* Requests
* GitHub REST API

 