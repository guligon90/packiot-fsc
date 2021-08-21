#!/bin/bash

set -eo pipefail

HOST="$(hostname -s)"
USER="${POSTGRES_USER:-postgres}"

export PGPASSWORD="${POSTGRES_PASSWORD:-}"

if [ -n "$DATABASE_CSL" ]; then
    echo "Initiating healthcheck in databases: $DATABASE_CSL"
    
    for DB in $(echo $DATABASE_CSL | tr ',' ' '); do
        DBNAME="${DB:-$POSTGRES_USER}"

        ARGS=(
            --host="$HOST"
            --username="$USER"
            --dbname="$DBNAME"
            --quiet --no-align --tuples-only
        )

        SELECT="$(echo 'SELECT 1' | psql "${ARGS[@]}")"

        if [ "$SELECT" != '1' ]; then
            echo "  Failed for $DB"    
            exit 1
        fi

        echo "  OK for $DB"
    done

    echo "Healthcheck completed"
    exit 0
fi