INICIAR O PROJETO
----------------------------------------------
python -m venv venv
. venv/Scripts/activate
pip install django
django-admin startproject project .
python manage.py startapp contact
----------------------------------------------
obs: sempre entrar no ambiente virtual = DjangoAgenda\Scripts\activate

CONFIGURAR O GIT
---------------------------------------------------
git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
# Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT
-----------------------------------------------------

MIGRANDO A BASE DE DADOS DO DJANGO (Qualquer alteração no models você tem que migrar)
------------------------------------------------------
python manage.py makemigrations
python manage.py migrate
------------------------------------------------------



CRIANDO E MODIFICANDO A SENHA DE UM SUPER USER DJANGO
----------------------------------------------------
python manage.py createsuperuser
python manage.py changepassword USERNAME
---------------------------------------------------
