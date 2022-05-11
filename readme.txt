python -m venv venv
.\venv\Scripts\activate
pip install django / pip install -r requirements.txt
pip freeze
django-admin startproject postcard
python manage.py createsuperuser : admin/admin




python manage.py makemigrations
python manage.py migrate
python manage.py runserver


MVC - Model-View-Controller
Django MTV - Model-Template-View