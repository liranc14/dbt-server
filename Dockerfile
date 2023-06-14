FROM python:3.10-slim-buster

COPY dbt_project /dbt_project
COPY requirements.txt app.py /dbt_project/

WORKDIR /dbt_project

RUN apt-get -y update
RUN apt-get -y install git
RUN pip install -r requirements.txt

# placeholder to allow dbt deps
COPY profiles.yml /root/.dbt/profiles.yml
RUN dbt deps

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--timeout", "0", "--workers", "6", "app:app"]