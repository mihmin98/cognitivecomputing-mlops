FROM python:3.10

WORKDIR /code

# COPY ./Pipfile ./Pipfile.lock /code/
COPY Pipfile.app /code/Pipfile
COPY Pipfile.lock.app /code/Pipfile.lock
RUN bash set_pipfile_env.sh ml
RUN python -m pip install --upgrade pip
RUN pip install pipenv 
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

COPY ./app /code/app
COPY ./model /code/model

CMD ["pipenv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]