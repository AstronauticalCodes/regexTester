 <div align="center">

# Regex Tester

![Python](https://img.shields.io/badge/python-3.x-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/framework-Django-092E20?logo=django&logoColor=white)
![GitHub last commit](https://img.shields.io/github/last-commit/AstronauticalCodes/regexTester)
![GitHub repo size](https://img.shields.io/github/repo-size/AstronauticalCodes/regexTester)
![GitHub stars](https://img.shields.io/github/stars/AstronauticalCodes/regexTester?style=social)

A **Django-based web application** for testing and validating regular expressions. It gives users a simple browser-based interface to submit a regex pattern together with sample text and see how the pattern behaves, backed by Django's built-in authentication and admin tooling.
</div>

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Configuration](#configuration)
- [Known Issues & Notes](#known-issues--notes)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Overview

Regex Tester provides a simple and intuitive interface for testing regular expressions against different text inputs, with results shown instantly rather than requiring a separate script or REPL. As a full Django project, it also ships with standard user account management and a Django admin panel for managing underlying records.

## Features

- **Regex Testing** — Submit a pattern and a block of sample text and see the results of the match instantly, without leaving the browser.
- **User Management** — Built-in account creation, login, and authorization via Django's authentication framework, so testing activity can be tied to a user.
- **Admin Interface** — Django's admin site is wired up for managing users and stored records directly, without needing to write custom admin views.

## Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python 3 |
| Web framework | Django |
| Database (development) | SQLite (`db.sqlite3`) |
| Frontend | Django templates (server-rendered) |
| Package management | `pip` + `requirements.txt` |

## Project Structure

The project follows a conventional Django layout, nested inside a `Regex Tester (Django)/task` directory at the repo root:

```
regexTester/
├── Regex Tester (Django)/
│   └── task/
│       ├── manage.py          # Django's command-line management utility
│       ├── db.sqlite3         # Default development database
│       ├── requirements.txt   # Python package dependencies
│       ├── <app>/             # Django app containing the regex-tester logic
│       │   ├── admin.py       # Django admin site configuration
│       │   ├── apps.py        # App configuration
│       │   ├── forms.py       # Form definitions (e.g. the regex/test-string input form)
│       │   ├── models.py      # Data models
│       │   ├── views.py       # Request handling / regex evaluation logic
│       │   ├── urls.py        # App-level URL routing
│       │   └── migrations/    # Database schema migrations
│       └── <project>/         # Django project settings package
│           ├── settings.py
│           ├── urls.py
│           └── wsgi.py / asgi.py
└── README.md
```

> This reflects standard Django scaffolding built around the files the project itself documents (`manage.py`, `db.sqlite3`, `admin.py`, `apps.py`, `forms.py`). Exact app/module names may differ slightly from the placeholders above — check the repository directly for the authoritative file tree.

## Requirements

- Python 3.x
- Django (pinned version specified in `requirements.txt`)
- `pip` and `venv` (or your preferred virtual environment tool)

## Getting Started

1. **Clone the repository**

   ```bash
   git clone https://github.com/AstronauticalCodes/regexTester.git
   ```

2. **Navigate to the project directory**

   ```bash
   cd regexTester/Regex\ Tester\ \(Django\)/task
   ```

   > The folder name contains spaces and parentheses, so remember to quote or escape it — the command above is written for bash/zsh. On Windows (cmd/PowerShell), wrap the path in quotes instead: `cd "regexTester\Regex Tester (Django)\task"`.

3. **Create a virtual environment**

   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment**

   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

5. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

6. **Apply database migrations**

   ```bash
   python manage.py migrate
   ```

7. **Create a superuser** (for admin access)

   ```bash
   python manage.py createsuperuser
   ```

8. **Run the development server**

   ```bash
   python manage.py runserver
   ```

9. **Open the app** — visit `http://127.0.0.1:8000` in your browser.

## Usage

- Visit the app's homepage, enter a regex pattern and a piece of sample text, and submit the form to see the match results.
- Depending on how authorization is configured, you may need to create an account and log in before testing (see **User Management** above).
- Visit `http://127.0.0.1:8000/admin` and log in with the superuser credentials created above to manage users and stored records through Django's admin interface.

## Configuration

Key files involved in running and customizing the app:

- `db.sqlite3` — the default development database.
- `manage.py` — Django's command-line utility for migrations, running the server, creating superusers, etc.
- `admin.py` — registers models with the Django admin site.
- `apps.py` — Django app configuration.
- `forms.py` — form definitions used to collect the regex pattern and test input.
- `requirements.txt` — pinned Python dependencies to install via `pip`.

For production use, the default SQLite database and any `DEBUG`/`SECRET_KEY` settings in `settings.py` should be replaced with production-appropriate values (e.g. via environment variables) rather than left at their development defaults.

## Known Issues & Notes

- The current README references a `LICENSE` file, but no `LICENSE` file exists in the repository at the time of writing — the link resolves to a 404. Add a `LICENSE` file (e.g. `MIT`) if you intend the stated license to actually apply.
- The project directory name (`Regex Tester (Django)/task`) contains spaces and parentheses, which requires extra quoting/escaping in shell commands — see the note in [Getting Started](#getting-started).

## Roadmap

Ideas for further hardening the project:

- [ ] Add a `LICENSE` file matching the license actually intended for the project
- [ ] Add an automated test suite (Django's built-in `TestCase` or `pytest-django`)
- [ ] Add a CI workflow (e.g. GitHub Actions) to run tests and linting on every push/PR
- [ ] Move secrets and environment-specific settings (`SECRET_KEY`, `DEBUG`, database config) out of `settings.py` and into environment variables
- [ ] Add support for toggling common regex flags (e.g. `IGNORECASE`, `MULTILINE`, `DOTALL`) in the UI, if not already available
- [ ] Deploy a live demo (e.g. Render, Railway, PythonAnywhere) and link it from this README

## Contributing

Contributions are welcome:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear, descriptive messages.
4. Push your changes to your fork.
5. Open a pull request against the main repository describing what changed and why.

## License

This repository does not currently include a `LICENSE` file. Until one is added, the code defaults to standard copyright — all rights reserved by the author. Add a `LICENSE` file (e.g. MIT or Apache-2.0) to formally permit reuse and clarify terms for contributors and users.

## Contact

For questions, bugs, or feature requests, please open an issue in the GitHub repository.
