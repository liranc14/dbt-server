docker run --rm \
           -p 5000:5000 \
           -v $(pwd)/profiles.yml:/root/.dbt/profiles.yml \
            $(docker build -q . -t dbt-service)


# docker build . -t dbt-service

# docker run --rm -p 5000:5000 -v $(pwd)/profiles.yml:/root/.dbt/profiles.yml dbt-service