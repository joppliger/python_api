# Je pars d'une image de base (python sur alpine)
FROM python:3.13.3-alpine

# Je crée mon répertoire de travail
WORKDIR /code

# 
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# J'installe mes requirements
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Je lance mon code 
COPY ./app app
CMD ["fastapi", "run", "app/main.py", "--port", "80", "--host", "0.0.0.0"]