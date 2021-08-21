# Base imports
import os
from typing import List, Optional

# Project imports
from docker.common import DatabaseConfig, must_have_db_credentials, PROJECT_HOME
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


def dump(arguments: Optional[List[str]]) -> int:

    dump_command = f'''
    PGPASSWORD="{DatabaseConfig.PASSWORD}" \\
    pg_dump \\
        -U {DatabaseConfig.USER.value} \\
        -h localhost \\
        -p {DatabaseConfig.PORT.value} \\
        {DatabaseConfig.NAME.value} \\
        -f {dump_file(DatabaseConfig.NAME.value)} \\
        -Fc \\
        -Z 9 \\
        --no-owner \\
        --no-privileges \\
        --verbose
    '''

    print(f">>>>>>>>>> Dumping data from DB {DatabaseConfig.NAME.value} <<<<<<<<<<")

    if arguments:
        dump_command += ' '.join(arguments)

    return run_local(dump_command)


def load(arguments: Optional[List[str]]) -> int:
    db_name = DatabaseConfig.NAME.value

    load_command = f'''
    PGPASSWORD={DatabaseConfig.PASSWORD.value} \\
    pg_restore \\
        -Fc \\
        -U {DatabaseConfig.USER.value} \\
        -h {DatabaseConfig.HOST.value} \\
        -p {DatabaseConfig.PORT.value} \\
        --no-owner \\
        --role={DatabaseConfig.USER.value} \\
        -d {db_name} < {dump_file(db_name)} \\
        --verbose
    '''

    print(f">>>>>>>>>> Loading data into DB {db_name} <<<<<<<<<<")

    if arguments:
        load_command += ' '.join(arguments)

    return run_local(load_command)


@must_have_db_credentials
def createtables(arguments: Optional[List[str]] = None) -> int:
    db_name = DatabaseConfig.NAME.value

    creation_cmd = f'''
    docker exec \\
        -it pgsqlserver-ctnr \\
        sh -c " \\
        PGPASSWORD={DatabaseConfig.PASSWORD.value} \\
        psql \\
            -U {DatabaseConfig.USER.value} \\
            -d {db_name} \\
            -f /ddl-stmts.sql \\
        "
    '''

    print(f">>>>>>>>>> Creating tables in DB {db_name} <<<<<<<<<<")

    if arguments:
        creation_cmd += ' '.join(arguments)

    return run_local(creation_cmd)


def dropdb(arguments: Optional[List[str]] = None) -> int:
    db_name = DatabaseConfig.NAME.value

    creation_cmd = f'''
    docker exec \\
        -it pgsqlserver-ctnr \\
        sh -c " \\
        dropdb \\
            {db_name} \\
            --if-exists \\
        "
    '''

    # -U {DatabaseConfig.USER.value} \\
    # -w {DatabaseConfig.PASSWORD.value} \\

    print(f">>>>>>>>>> Dropping DB {db_name} <<<<<<<<<<")

    if arguments:
        creation_cmd += ' '.join(arguments)

    return run_local(creation_cmd)
