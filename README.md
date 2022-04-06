**Install the Requirements using terminal** 
sudo apt install -y python3-pip #on linux or download latest python version from pythhon.org
python3 --version
pip3 install pipenv
mkdir hospital
cd hospital
pipenv install django
pipenv shell

**Start project***
django-admin startproject hospital .
python manage.py runserver #copy the url generated to browser to view page
pip env --venv #then copy the path for use in Vscode
ctrl + C #stops server from terminal

**in VScode**
search python interpreter and copy path from <pipenv--Venv> , include </bin/python> at the end and enter
python manage.py runserver #copy the url generated to browser to view page


**Make database migrations** # create the database so we can start using it
#activate the virtual environment, go to the folder where the manage.py file is, and run the commands below:
python manage.py makemigrations
python manage.py sqlmigrate hospital 0001
python manage.py migrate

**For Admin Account, please create one with superuser!**
python manage.py createsuperuser

**Run the application**
python manage.py runserver

"""**tests installation**
django-admin.py --version 

virtualenv venv -p python3
source venv/bin/activate
pip install Django==4.0.3
django-admin startapp hospital
"""
