FROM python:3.10-slim-buster

COPY dbt_project /dbt_project
COPY requirements.txt /dbt_project/

WORKDIR /dbt_project

RUN apt-get -y update
RUN apt-get -y install git
RUN pip install -r requirements.txt

# placeholder to allow dbt deps
COPY profiles_placeholder.yml /root/.dbt/profiles_placeholder.yml
RUN mv /root/.dbt/profiles_placeholder.yml /root/.dbt/profiles.yml
RUN dbt deps

COPY gunicorn.py /dbt_project/
COPY app.py /dbt_project/

EXPOSE 5000

CMD ["gunicorn", "-c", "gunicorn.py", "app:app"]