#!/bin/bash

set -eo pipefail

HOST="$(hostname -s)"
USER="${POSTGRES_USER:-postgres}"

export PGPASSWORD="${POSTGRES_PASSWORD:-}"

if [ -n "$DATABASE" ]; then
    echo "Initiating healthcheck in database: $DATABASE"
    
    DBNAME="${DATABASE:-$POSTGRES_USER}"

    ARGS=(
        --host="$HOST"
        --username="$USER"
        --dbname="$DBNAME"
        --quiet --no-align --tuples-only
    )

    SELECT="$(echo 'SELECT 1' | psql "${ARGS[@]}")"

    if [ "$SELECT" != '1' ]; then
        echo "  Failed for $DATABASE"    
        exit 1
    fi

    echo "Healthcheck completed "
    exit 0
fi
