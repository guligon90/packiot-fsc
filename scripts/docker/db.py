# Base imports
from typing import List, Optional, Text

# Project imports
from docker.common import usage
from docker.config.db import DBCONFIG
from docker.run import run_local


DB_USAGE_TEXT = '''
docker.db.db_action
Runs actions over the packiotfscdb database.

Usage:
    $ ./scripts/devenv.py db [action] [resource]
    $ python ./scripts/devenv.py db [action] [resource]

Where:
    action: create | load
    resource: tables | data
'''


SUPPORTED_ARGS = {
    'create': {
        'tables': 'ddl-stmts.sql',
    },
    'load': {
        'data': 'dml-stmts.sql',
    },
}


def _build_command(sql_file: str, arguments: Optional[List[str]] = None) -> Text:
    command = f'''
    docker exec \\
        -it pgsqlserver-ctnr \\
        sh -c " \\
        PGPASSWORD={DBCONFIG.PASSWORD} \\
        psql \\
            -U {DBCONFIG.USERNAME} \\
            -d {DBCONFIG.NAME} \\
            -f {sql_file} \\
        "
    '''

    if arguments:
        command += ' '.join(arguments[2:])

    return command


@DBCONFIG.must_have_db_credentials
def db_action(arguments: List[str]) -> int:
    try:
        action = arguments[0]
        resource = arguments[1]
    except IndexError:
        usage(DB_USAGE_TEXT)
        return -1

    print(f'>>>>>>>>> Running {action} {resource} <<<<<<<<<<')

    resources = SUPPORTED_ARGS.get(action, {})
    sql_file = resources.get(resource, '')

    if sql_file != '':
        command = _build_command(sql_file, arguments)
        return run_local(command)

    usage(DB_USAGE_TEXT)
    return -1
