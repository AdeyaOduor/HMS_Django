**Install the Requirements** 
sudo apt install -y python3-pip
sudo apt install -y python3-venv
pip install Django==4.0.3

**tests installation**
django-admin.py --version 

**Make database migrations**
python manage.py makemigrations
python manage.py migrate

**Create HMS project**
django-admin startproject HMS

**For Admin Account, please create one with superuser!**
python manage.py createsuperuser

**Run the application**
python manage.py runserver


