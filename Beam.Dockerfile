FROM armswdev/pytorch-arm-neoverse:r23.03-torch-1.13.0-openblas
COPY . /app
WORKDIR /app
RUN pip install -U pip
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "beam_pipeline.py"]