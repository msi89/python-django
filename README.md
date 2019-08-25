#installer python, python-pip
```bash
 sudo apt-get install python3 python3-pip
```

#installer virtualenv
sudo pip3 instal virtualenv

#Creer un environnement virtual
```bash
virtualenv -p python3 env
```
#initialiser git et ajouter un fichier .gitignore
```bash
git init && touch .gitignore
```
#installer django
```bash
pip install django
```
#creer la structure de votre projet
```bash
django-admin startproject nom__du_projet
```

#installer postgres SQL
```bash
#1-contrib: permet d'ajouter des packages tiers 
 sudo apt install postgresql postgresql-contrib
 sudo -u postgres psql

#2-creer un utiliser pgsl
sudo -u postgres createuser --interactive

# 3- creer une base de donnees
createdb nom-bdd
```
#Afin d'utiliser une base PostgreSQL dans un projet Django, il faut installer la librairie Psycopg2 :
```bash
 pip install psycopg2
```
# demarrer le serve python
```bash
cd mysite
./manage.py runserver
```
# Ctrl+C pour arreter le serveur et lancer les migrations
```bash
./manage.py migrate
```
# installer toolbar for django developer
```bash
pip install django-debug-toolbar
```

#creer une nouvelle application
```bash
django-admin startapp nom_app
```
# il faut declarer notre application dans settings ~~INSALLED_APPPS = [ ..., store.app.StoreConfig]