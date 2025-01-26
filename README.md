# Regex Tester

## Overview
The Regex Tester is a Django-based web application designed to help users test and validate regular expressions (regex). This application provides a simple and intuitive interface for testing regex patterns against various text inputs.

## Features
- **Regex Testing**: Test your regular expressions against different text inputs to see the results instantly.
- **User Management**: Built-in user management with authentication and authorization.
- **Admin Interface**: Manage records and users using Django's admin interface.

## Installation
To get started with the Regex Tester, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AstronauticalCodes/regexTester.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd regexTester/Regex\ Tester\ \(Django\)/task
   ```
3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```
4. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
5. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
6. **Apply the migrations**:
   ```bash
   python manage.py migrate
   ```
7. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```
8. **Run the development server**:
   ```bash
   python manage.py runserver
   ```
9. **Access the application**:
   Open your web browser and navigate to `http://127.0.0.1:8000`.

## Configuration
The project includes several configuration files to ensure smooth development and deployment:
- `db.sqlite3`: The main SQLite database file.
- `manage.py`: The Django command-line utility for administrative tasks.
- `admin.py`: Configuration for the Django admin interface.
- `apps.py`: Application configuration.
- `forms.py`: Form definitions for the application.

## Contributing
We welcome contributions from the community. To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear and concise messages.
4. Push your changes to your forked repository.
5. Create a pull request to the main repository.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact
For any questions or feedback, please open an issue in the GitHub repository.

---
