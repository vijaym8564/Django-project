docker run -d   --name mysql-container   -e MYSQL_ROOT_PASSWORD=root123   -e MYSQL_DATABASE=myapp_db   -e MYSQL_USER=django_user   -e MYSQL_PASSWORD=StrongPassword123!   -p 3306:3306   mysql:8.0

docker run -p 8000:8000   --env-file .env   --name django-app   --link mysql-container:mysql   devops-with-vj
