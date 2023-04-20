FROM --platform=linux/amd64 armswdev/pytorch-arm-neoverse:r23.03-torch-1.13.0-openblas
COPY . /app
WORKDIR /app
RUN pip install -U pip
RUN pip install --timeout 600 -r requirements.txt
ENTRYPOINT ["python", "pipeline.py"]
