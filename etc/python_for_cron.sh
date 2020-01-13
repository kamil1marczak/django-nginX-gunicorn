#!/bin/bash
cd ../
docker build -t cron_image_entrypoint/develop .
docker stop prod_container_cron || true 

docker run --env-file .env  --rm -ti -d -p 8000:8040 --name prod_container_cron cron_image_entrypoint/develop
docker exec -it prod_container_cron bash -c "python3 /src/weather_archive_crone.py"
docker stop prod_container_cron





