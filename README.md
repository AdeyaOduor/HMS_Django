**Install the Requirements** 
sudo apt install -y python3-pip
sudo apt install -y python3-venv OR sudo pip3 install virtualenv

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

**Make database migrations**
python manage.py makemigrations
python manage.py migrate

**Create HMS project**
django-admin startproject HMS

**For Admin Account, please create one with superuser!**
python manage.py createsuperuser

**Run the application**
python manage.py runserver


