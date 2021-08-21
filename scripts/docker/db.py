# Base imports
import os
from typing import List, Optional

# Project imports
from docker.common import PROJECT_HOME
from docker.config.db import DBCONFIG
from docker.run import run_local


DUMP_USAGE_TEXT = '''
docker.db_data.dump:
    Dumps the database content in a .dump file, given valid credentials.

Usage:
    $ ./scripts/devenv.py dump
    $ python /scripts/devenv.py dump
'''


LOAD_USAGE_TEXT = '''
docker.db_data.load:
    Restores DB data from a .dump file, given a valid DB name.

Usage:
    $ ./scripts/devenv.py load
    $ python /scripts/devenv.py load
'''


def dump_file(db_name: str) -> str:
    return os.path.join(PROJECT_HOME, f'{db_name}.dump')


@DBCONFIG.must_have_db_credentials
def dump(arguments: Optional[List[str]]) -> int:

    dump_command = f'''
    PGPASSWORD="{DBCONFIG.PASSWORD}" \\
    pg_dump \\
        -U {DBCONFIG.USERNAME} \\
        -h localhost \\
        -p {DBCONFIG.PORT} \\
        {DBCONFIG.NAME} \\
        -f {dump_file(DBCONFIG.NAME)} \\
        -Fc \\
        -Z 9 \\
        --no-owner \\
        --no-privileges \\
        --verbose
    '''

    print(f">>>>>>>>>> Dumping data from DB {DBCONFIG.NAME} <<<<<<<<<<")

    if arguments:
        dump_command += ' '.join(arguments)

    return run_local(dump_command)


@DBCONFIG.must_have_db_credentials
def load(arguments: Optional[List[str]]) -> int:
    db_name = DBCONFIG.NAME

    load_command = f'''
    PGPASSWORD={DBCONFIG.PASSWORD} \\
    pg_restore \\
        -Fc \\
        -U {DBCONFIG.USERNAME} \\
        -h {DBCONFIG.PGHOST} \\
        -p {DBCONFIG.PORT} \\
        --no-owner \\
        --role={DBCONFIG.USERNAME} \\
        -d {db_name} < {dump_file(db_name)} \\
        --verbose
    '''

    print(f">>>>>>>>>> Loading data into DB {db_name} <<<<<<<<<<")

    if arguments:
        load_command += ' '.join(arguments)

    return run_local(load_command)


@DBCONFIG.must_have_db_credentials
def createtables(arguments: Optional[List[str]] = None) -> int:
    db_name = DBCONFIG.NAME

    creation_cmd = f'''
    docker exec \\
        -it pgsqlserver-ctnr \\
        sh -c " \\
        PGPASSWORD={DBCONFIG.PASSWORD} \\
        psql \\
            -U {DBCONFIG.USERNAME} \\
            -d {db_name} \\
            -f /ddl-stmts.sql \\
        "
    '''

    print(f">>>>>>>>>> Creating tables in DB {db_name} <<<<<<<<<<")

    if arguments:
        creation_cmd += ' '.join(arguments)

    return run_local(creation_cmd)


def dropdb(arguments: Optional[List[str]] = None) -> int:
    db_name = DBCONFIG.NAME

    creation_cmd = f'''
    docker exec \\
        -it pgsqlserver-ctnr \\
        sh -c " \\
        dropdb \\
            {DBCONFIG.NAME} \\
            --if-exists \\
        "
    '''

    print(f">>>>>>>>>> Dropping DB {db_name} <<<<<<<<<<")

    if arguments:
        creation_cmd += ' '.join(arguments)

    return run_local(creation_cmd)
