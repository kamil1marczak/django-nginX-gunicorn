#!/bin/bash

docker build -t models_image_entrypoint/develop .
docker stop models_container || true 


docker run --env-file .env  --rm -ti -d -p 70:8090 --name models_container models_image_entrypoint/develop
docker exec -it models_container bash -c "python3 /src/manage.py makemigrations"
docker exec -it models_container bash -c "python3 /src/manage.py migrate"
docker exec -it models_container bash -c "python3 /src/superuser.py"
docker exec -it models_container bash -c "python3 /src/populate_citys.py"





