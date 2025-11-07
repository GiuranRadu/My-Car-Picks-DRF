# Django REST Framework Project

This project is part of the NewTech Academy course on Django and Django REST Framework.

## 🚀 Getting Started

### 1. Clone the repository
git clone https://github.com/GiuranRadu/My-Car-Picks-DRF.git
cd MyCarPicks
``

### 2. Create and activate a virtual environment (same level as the project folder)”
-- MyCarPicks
    |__ manage.py
    |__ mycarpicks/
    |__ accounts/
    |__ ...
-- venv/

source venv/bin/activate (pe MacOS)
source venv/Source/activate (pe Windows)
PS: Trebuie sa fim la acelasi nivel cu folderul venv


### 3. Install dependencies
pip install -r requirements.txt
If you don’t have the file yet, generate it with: pip freeze > requirements.txt


### 4. Run Migrations
Before creating any user or using the admin panel, you need to initialize the database by running migrations.
python manage.py makemigrations
python manage.py migrate


### 5. Create a Superuser
python manage.py createsuperuser
After this, you can log into the Django admin panel at http://127.0.0.1:8000/admin/


### 6. Run the server
python manage.py runserver


### Update made by GiuranRaduTest - testing Pull Request