#!/bin/bash

set -e
set -u

function create_user_and_database() {
	local database=$1
    local user=$POSTGRES_USER
	
    echo "Creating database '$database'"
	
    psql -v ON_ERROR_STOP=1 --username "$user" <<-EOSQL
	    CREATE DATABASE $database;
	    GRANT ALL PRIVILEGES ON DATABASE $database TO $user;
EOSQL
}

if [ -n "$DATABASE_CSL" ]; then
    echo "Multiple database creation requested: $DATABASE_CSL"
    
    for db in $(echo $DATABASE_CSL | tr ',' ' '); do
        create_user_and_database $db
    done
    
    echo "Multiple databases created"
fi
