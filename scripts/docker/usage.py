# Base imports
from typing import List

RED = '\033[91m'
BLUE = '\033[94m'
END = '\033[0m'


def red(string: str) -> str:
    return RED + string + END


def blue(string: str) -> str:
    return BLUE + string + END


def usage(_: List[str] = None) -> None:
    print('''
    Usage:
        python3 devenv.py <command> <arguments>
        devenv.py <command> <arguments>

    Commands:
        build                     Downloads and builds images.
        clean                     Removes all containers, networks {volumes}.
        coverage                  Reports the test coverage of the service.
        createtables              Runs the SQL statements for creating tables in the database.
        dev                       Starts containers.
        dump                      Dumps data from a DB, accessible via one of the cloud sql proxy services.
        dropdb                    Drops the current PostgreSQL database, if it exists.
        load                      Restores data to a informed database in the local DB service.
        erd                       Generates an ER diagram (ERD) of the implemented DB models.
        kill                      Runs clean and {images}.
        licenses                  Runs license check in backend or frontend.
        lint                      Runs linter in backend or frontend.
        logs                      Attaches logs to terminal.
        make_migrations           Generates migration files if there are modifications in the DB models.
        migrate                   Apply the generated migrations in the databases.
        show_migrations           Lists the existing migrations in the project or in a specific app, if informed.
        restart                   Restarts containers.
        run                       Runs an arbitrary command in a specified service (eg. 'run pgsqlserver build').
        shell                     Runs the Django command prompt (shell).
        start                     Start containers in detached mode.
        startwlogs                Start containers in detached mode, showing the logs.
        status                    Shows all containers, images, networks and volumes.
        stop                      Stops all containers.
        su                        Creates a Django Admin super user.
        test                      Runs the test runner in all services
    '''.format(
        volumes=red('and volumes'),
        images=red('removes all images'),
    ))
