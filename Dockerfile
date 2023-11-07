FROM python:3.11-slim

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile","Pipfile.lock","./"]

RUN pipenv install --system --deploy

COPY ["*.py","*.pkl","./"]

EXPOSE 9696 

ENTRYPOINT ["pipenv","run","gunicorn", "--bind", "0.0.0.0:9696", "predict:app"] 