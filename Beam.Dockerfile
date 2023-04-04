FROM armswdev/pytorch-arm-neoverse:r23.03-torch-1.13.0-openblas
COPY . /app
WORKDIR /app
RUN pip install -U pip
RUN pip install -r requirements.txt
# ENTRYPOINT ["python", "beam_pipeline.py"]
CMD ["python", "beam_pipeline.py"]



# docker build --tag search-etl -f Beam.Dockerfile .
# docker run --network elk_elastic --env-file .env search-etl