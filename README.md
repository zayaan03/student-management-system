# Student Management System

A simple Django-based student management application for creating, updating, deleting, and exporting student records.

## Features

- Add new students with fields: Student ID, Name, Email, Department, Semester, CGPA
- Edit existing student records
- Delete student records with confirmation
- Export student data as CSV or plain text
- Built-in Django admin support for managing students

## Project Structure

- `manage.py` - Django command-line utility
- `config/` - Django project configuration
  - `settings.py` - Project settings
  - `urls.py` - Root URL routes
- `students/` - Main application
  - `models.py` - `Student` model definition
  - `forms.py` - Student form for create/edit operations
  - `views.py` - List, add, edit, delete, and export views
  - `urls.py` - Student app URL routes
  - `templates/` - HTML templates for the app
  - `static/` - Static assets like CSS

## Requirements

- Python 3.10+ (or a supported version for Django 6.x)
- Django 6.0.x
- SQLite (default database included as `db.sqlite3`)

## Installation

1. Clone or copy the repository:

```bash
git clone <repository-url>
cd studentmanagementsystem
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install Django:

```bash
pip install django==6.0.6
```

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Create a superuser for admin access (optional):

```bash
python manage.py createsuperuser
```

## Running the Application

Start the development server:

```bash
python manage.py runserver
```

Open the app in your browser:

- Main interface: `http://127.0.0.1:8000/`
- Admin interface: `http://127.0.0.1:8000/admin/`

## Usage

- Add students via the list page form
- Edit students by choosing the edit action for a row
- Delete students with the delete confirmation page
- Export data using the CSV or TXT export links

## Student Model

The `Student` model includes the following fields:

- `student_id` - unique student identifier
- `name` - student name
- `email` - student email address
- `department` - department name
- `semester` - current semester
- `cgpa` - cumulative grade point average

## Notes

- This project uses SQLite by default (`db.sqlite3`)
- `DEBUG` is enabled in `config/settings.py`; do not use this setting in production
- The app is intentionally small and designed for learning/demo purposes


This repository does not include a license file. Add a `LICENSE` if you want to clarify reuse terms.
