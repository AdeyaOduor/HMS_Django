**Install the Requirements using linux terminal** 
sudo apt install -y python3-pip
python3 --version
pip3 install pipenv

**tests installation**
django-admin.py --version 

**Start project***
mkdir HMS
cd HMS
virtualenv venv -p python3
source venv/bin/activate
pip install Django==4.0.3
django-admin startproject HMS
django-admin startapp hospital

**Make database migrations** # create the database so we can start using it
#activate the virtual environment, go to the folder where the manage.py file is, and run the commands below:
python manage.py makemigrations
python manage.py sqlmigrate hospital 0001
python manage.py migrate

**Create HMS project**
django-admin startproject HMS

**For Admin Account, please create one with superuser!**
python manage.py createsuperuser

**Run the application**
python manage.py runserver


