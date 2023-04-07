
# Step 1.
# Create a .env file with secrets

# Step 2.
# cd ./model directory and run Download model
# python ./model/download_pretrain_model.py

# Step 3.
# cd ./elk docker-compose -f docker-compose-elk.yaml up -d
# check http://127.0.0.1:9200 for elasticsearch
# check http://127.0.0.1:5601 for kibana

# Step 4.
# Build Airflow

# Step 5.
# docker build --tag search-etl -f Pipeline.Dockerfile .
# docker run --rm --network elk_elastic --env-file .env search-etl