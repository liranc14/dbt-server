docker run --rm \
           -p 5000:5000 \
            $(docker build -q . -t dbt-service)


# docker build . -t dbt-service

# docker run --rm -p 5000:5000 \
#     -e DBT_TYPE='' \
#     -e DBT_HOSTNAME='' \
#     -e DBT_USERNAME='' \
#     -e DBT_PASSWORD='' \
#     -e DBT_PORT= \
#     -e DBT_DATABASE='' \
#     -e DBT_SCHEMA='' \
#     -t dbt-service
