FROM python:3.11-slim

RUN apt update && apt upgrade -y
RUN pip install --no-cache-dir pipenv

WORKDIR /usr/src/app
COPY Pipfile Pipfile.lock ./
COPY . .

RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy


ENV PYTHONUNBUFFERED=1
ENTRYPOINT [ "pipenv","run","python","-u","./app.py" ]