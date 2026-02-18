# PSUSphere

This repository contains a Django project for PSUSphere.

## 1. Setting Up

1. **Create a virtual environment** (choose a location you prefer):

   ```bash
   virtualenv psusenv
   # or
   python -m venv psusenv
   ```

   A new directory named `psusenv/` will be created:

   ```
   psusenv/
   │
   ├── bin/            # (Linux/macOS) python executable & activation scripts
   │   ├── activate
   │   ├── python
   │   └── pip
   │
   ├── Scripts/        # (Windows) python.exe & activation scripts
   │   ├── activate.bat
   │   ├── activate.ps1
   │   └── python.exe
   │
   ├── lib/            # installed Python packages
   ├── include/        # C headers for building packages
   └── pyvenv.cfg      # configuration file
   ```

2. **Clone this repository** (you can clone inside the virtual environment directory or anywhere else):

   ```bash
   cd psusenv
   git clone <github-url>
   ```

   After cloning you should have:

   ```
   psusenv/
   │
   ├── ...
   └── PSUSphere/    # your cloned repo
   ```

3. **Activate the virtual environment**

   - Windows (PowerShell):
     ```powershell
     .\psusenv\Scripts\activate.ps1
     ```

   - Windows (cmd):
     ```cmd
     psusenv\Scripts\activate.bat
     ```

   - macOS/Linux:
     ```bash
     source psusenv/bin/activate
     ```

   You should see the environment name in your prompt:
   `(psusenv) C:\Users\...>`

4. **Install Django**

   ```bash
   pip install django
   ```

5. **Create the Django project** (already done in this repo):

   ```bash
   cd PSUSphere
   django-admin startproject psusphere .
   ```

## Legend

- ✅ Add code
- ❌ Remove code
- 🖥️ My screen looks like
- 📄 Existing code

---

Follow these steps to continue working on the PSUSphere Django application.

## 2. Creating an Application

1. Activate your virtual environment and change into the directory containing `manage.py`:

   ```bash
   cd PSUSphere
   # (psusenv) in prompt should already be visible
   ```

2. Run the startapp command:

   ```bash
   python manage.py startapp studentorg
   ```

3. Register the application by adding it to `INSTALLED_APPS` in `psusphere/settings.py`:

   ```python
   INSTALLED_APPS = [
       ...
       'studentorg',
   ]
   ```

4. **Create a `.gitignore` file** at the repository root (a sample Python template is already included in this repo).
   The ignore list should cover `__pycache__`, `db.sqlite3`, virtual environments, IDE files, etc.

## 3. Models and Admin

In `studentorg/models.py` define the following classes (a base model provides timestamps):

```python
from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class College(BaseModel):
    college_name = models.CharField(max_length=150)
    def __str__(self):
        return self.college_name

# ... Program, Organization, Student, OrgMember as shown earlier ...
```

Run migrations after editing models:

```bash
python manage.py makemigrations
python manage.py migrate
```

Register the models in `studentorg/admin.py` and enhance the admin interface:

```python
from django.contrib import admin
from .models import College, Program, Organization, Student, OrgMember

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ("college_name", "created_at", "updated_at")
    search_fields = ("college_name",)
    list_filter = ("created_at",)

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("prog_name", "college")
    search_fields = ("prog_name", "college__college_name")
    list_filter = ("college",)

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "college", "description")
    search_fields = ("name", "description")
    list_filter = ("college",)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "lastname", "firstname", "middlename", "program")
    search_fields = ("lastname", "firstname")

@admin.register(OrgMember)
class OrgMemberAdmin(admin.ModelAdmin):
    list_display = ("student", "get_member_program", "organization", "date_joined")
    search_fields = ("student__lastname", "student__firstname")

    def get_member_program(self, obj):
        try:
            member = Student.objects.get(id=obj.student_id)
            return member.program
        except Student.DoesNotExist:
            return None
```

Create a superuser and populate the admin site with sample data.

## 4. Generating Fake Data

Install the Faker package in your virtual environment:

```bash
pip install faker
```

Add a custom management command to `studentorg/management/commands/create_initial_data.py` (file included already).
Run it with:

```bash
python manage.py create_initial_data
```

Check the admin interface to confirm that colleges, programs, organizations, students, and memberships were created.

---
