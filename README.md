Simple network implementation using Django
--------------------------------

Clone this repository to your machine:

$ git clone https://github.com/DanyilS/follow-network.git
-

Used sqlite, docker contain only web-service, so before running the app - run it on your machine locally to create db: 

(venv) $ py manage.py migrate
(venv) $ py manage.py createsuperuser


$ docker build .
-
$ docker-compose up
-
Don't forget to add some users and posts to fully test the project

--------------------------------
or this image on docker hub: 

$ docker pull sdanik/network_web


