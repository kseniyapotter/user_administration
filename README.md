Small Django application to manage users and their bank account data (IBAN).

INSTALLATION

You need to install docker and docker-compose on your machine.

Rename local_settings.py.sample in local_settings.py.

Run the commands:

$ docker build -t useradmin .

$ docker-compose up -d

$ docker-compose exec web ./manage.py migrate

$ docker-compose exec web ./manage.py createsuperuser


Open http://127.0.0.1:8000/admin, login as superuser and create a group with permissions 'add', 'change', 'delete' for 'customer user'. Create users with 'Staff status' belong to this group. These users are the Administrators. Now you can login under the administrator and create/read/update/delete customer users.

Create google OAuth 2.0 in Google Developers Console (https://console.developers.google.com/)
Add key and secret to local_settings.py.
Fill fields on google OAuth:

'Under Authorized JavaScript origins fill'

http://127.0.0.1:8000


'Authorized redirect URIs'

http://127.0.0.1:8000/account/complete/google-oauth2/

