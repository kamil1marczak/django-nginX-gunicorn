#!/bin/bash
cd ../

docker build -t models_image_entrypoint/develop .
docker stop models_container || true 


docker run --env-file .env  --rm -ti -d -p 8000:8090 --name models_container models_image_entrypoint/develop
docker exec -it models_container bash -c "python3 /src/manage.py makemigrations"
docker exec -it models_container bash -c "python3 /src/manage.py migrate"
docker exec -it models_container bash -c "python3 /src/manage.py initial_deployment"
docker stop models_container






