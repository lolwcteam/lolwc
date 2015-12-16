sudo apt-get install python-dev python3-dev
sudo apt-get install python-pip
pip install virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
export VIRTUALENVWRAPPER_SCRIPT=/usr/local/bin/virtualenvwrapper.sh
source /usr/local/bin/virtualenvwrapper_lazy.sh
mkvirtualenv django
workon django
pip install django
pip install xmltodict
pip install requests
pip install json
pip install django-omnibus
sudo echo "source /usr/local/bin/virtualenvwrapper_lazy.sh" >> $HOME/.bashrc
git clone https://github.com/lolwcteam/lolwc
cd lolwc/wololol/
python manage.py omnibusd &
python manage.py runserver
echo "Done... Running on localhost:8000"

