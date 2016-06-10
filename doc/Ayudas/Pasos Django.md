#Primera vez

- sudo apt-get install python-pip
- sudo pip install virtualenvwrapper
- export WORKON_HOME=$HOME/.virtualenvs
- export PROJECT_HOME=$HOME/Devel
- export VIRTUALENVWRAPPER_SCRIPT=/usr/local/bin/virtualenvwrapper.sh
- source /usr/local/bin/virtualenvwrapper_lazy.sh
- mkvirtualenv TUCOSA
- workon TUCOSA
- pip install django
- django-admin.py startproject TUCOSADELPROYECTO
- cd TUCOSADELPROYECTO
- python manage.py runserver PUERTOSSIO


#El resto de las veces

- source /usr/local/bin/virtualenvwrapper_lazy.sh
- workon TUCOSA
- cd TUCOSADELPROYECTO
- python manage.py runserver PUERTOSSIO

#Otras cosas

- python manage.py //Muestra todos los comandos para hacer
- python manage.py startapp NOMBREAPPLIACION
- python manage.py syncdb
- python manage.py migrate
	- The migrate command looks at the INSTALLED_APPS setting and creates any necessary
	- database tables according to the database settings in your mysite/settings.py file and the
	- databasemigrations shipped with the app (we’ll cover those later). You’ll see a message for
	- each migration it applies.
- python manage.py runserver

#Opcional

- sudo nano /home/TUUSUARIO/.bashrc
- agregear en la ultima linea
- source /usr/local/bin/virtualenvwrapper_lazy.sh
- asi ya no hay que ponerla cada vez que se inicie el proyecto

#Crear aplicacion

- python manage.py startapp NOMBREAPPLIACION





