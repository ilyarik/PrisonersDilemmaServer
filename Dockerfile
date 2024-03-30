FROM python:3.12.2-slim
WORKDIR /home/server
ENV COMPOSE_HTTP_TIMEOUT=180
ENV DOCKER_CLIENT_TIMEOUT=180
ENV PIP_ROOT_USER_ACTION=ignore
COPY *.py ./
COPY Environments/*.py ./Environments/
COPY Players/*.py ./Players/
COPY requirements.txt ./requirements.txt
RUN pip install --disable-pip-version-check -q --no-input --no-cache-dir -r requirements.txt
CMD ["python", "./server.py"]
