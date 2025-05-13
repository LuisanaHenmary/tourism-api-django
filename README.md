# 🗺️ Tourism-api-django

A REST API built with Django and the Django REST Framework for managing tourist locations, categories, and reviews. It includes JWT authentication (djangorestframework-simplejwt) and automatic documentation with Swagger (drf-yasg).

## 📦 Technologies

- Django 5.2
- Django REST Framework
- PostgreSQL
- SimpleJWT (djangorestframework-simplejwt)
- drf-yasg (Swagger/OpenAPI)
- Python 3.11.4

## 🚀 Installation

git clone https://github.com/LuisanaHenmary/tourism-api-django.git \
cd tourism-api \
python -m venv env \
source env/bin/activate  # en Windows: env\Scripts\activate \
pip install -r requirements.txt

## ⚙️ Config

Define environment variables in the **.env** file

DEBUG=True \
SECRET_KEY=your_secret_key \
DATABASE_NAME=db_name \
DATABASE_USER=your_superuser \
DATABASE_PASSWORD=your_password \
DATABASE_HOST=localhost \
DATABASE_PORT=5432

## 🧪 Migrations and Superuser

python manage.py makemigrations \
python manage.py migrate \
python manage.py createsuperuser

## ▶️ Run server

python manage.py runserver

## 🗂️ Interactive documentation

- **Swagger UI:** /swagger/
- **Redoc:** /redoc/
