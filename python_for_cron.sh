#!/bin/bash

docker build -t cron_image_entrypoint/develop .
docker stop prod_container_cron || true 

docker run --rm -ti -d -p 40:8040 --name prod_container_cron cron_image_entrypoint/develop
docker exec -it prod_container_cron bash -c "python3 /src/flight_archive_crone.py"






