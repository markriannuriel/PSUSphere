# PSUSphere

A Django-based web application for managing college student organizations and memberships at Palawan State University (PSU).

## Description

PSUSphere is a comprehensive student organization management system that enables colleges to organize, track, and manage student organizations. The application provides a platform for administrators to manage colleges, academic programs, student organizations, student profiles, and organization memberships.

## Features

- **College Management**: Create and manage multiple colleges within the institution
- **Program Management**: Organize academic programs linked to specific colleges
- **Organization Tracking**: Register and manage student organizations with descriptions
- **Student Management**: Maintain a comprehensive student database with identification and program assignment
- **Organization Membership**: Track student memberships in various organizations with join dates
- **Admin Interface**: User-friendly Django admin interface for data management
- **Search & Filter**: Advanced search and filtering capabilities across all models
- **Data Generation**: Faker-based management command for populating test data

## Technology Stack

- **Framework**: Django 6.0.2
- **Database**: SQLite3
- **Python Version**: 3.14+
- **Additional Libraries**:
  - asgiref (3.11.1) - ASGI utilities
  - sqlparse (0.5.5) - SQL parsing
  - Faker (40.4.0) - Test data generation
  - tzdata (2025.3) - Timezone data

## Getting Started

### Prerequisites

- Python 3.14+
- pip package manager

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/markriannuriel/PSUSphere.git
   cd PSUSphere
   ```

2. Create and activate virtual environment
   ```bash
   python -m venv psusenv
   # On Windows
   psusenv\Scripts\activate
   # On macOS/Linux
   source psusenv/bin/activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Navigate to the project directory
   ```bash
   cd psusenv/PSUSphere
   ```

5. Run migrations
   ```bash
   python manage.py migrate
   ```

6. Create a superuser account
   ```bash
   python manage.py createsuperuser
   ```

7. (Optional) Load initial fake data
   ```bash
   python manage.py create_initial_data
   ```

8. Start the development server
   ```bash
   python manage.py runserver
   ```

9. Access the application
   - Admin Interface: http://127.0.0.1:8000/admin/
   - Login with your superuser credentials

## Models

- **College**: Represents academic colleges within the institution
- **Program**: Academic programs offered by colleges
- **Organization**: Student organizations that can belong to specific colleges
- **Student**: Student profiles with identification and program assignment
- **OrgMember**: Tracks student memberships in organizations

## Authors

- **Mark Rian Fernandez**
- **Dirl Ydrei Herrera**

## License

This project is created for educational purposes at Palawan State University.
