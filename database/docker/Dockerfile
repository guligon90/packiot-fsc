FROM postgres:11

LABEL maintainer="guligon90@gmail.com"

# Set timezone
ARG TZ
RUN \
    apt-get update \
    && apt-get install -y -q --no-install-recommends \
        tzdata \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone

# Copying shell scripts
COPY ./scripts/sh/*.sh ./ 

# Copying SQL statements (DDL and queries)
COPY ./scripts/sql/* ./

RUN \
    # Scripts for creating DBs and loading data into them (at service startup)
    mv ./create-db.sh ./docker-entrypoint-initdb.d/ \
    # Making scripts executable
    && chmod +x is-database-up.sh \
    && chmod +x ./docker-entrypoint-initdb.d/create-db.sh

EXPOSE 5433/tcp

# Two minutes should be enough to initialize the database
# 2min = 120s => 120s/5s = 24 retries...
HEALTHCHECK --interval=5s --timeout=5s --retries=24 CMD [ "./is-database-up.sh" ]
