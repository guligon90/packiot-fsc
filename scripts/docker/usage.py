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
        code                      Analyzes the codebase, performing linting or fixing.
        db                        Performs actions over the database.
        dev                       Starts containers.
        kill                      Runs clean and {images}.
        lint                      Runs linter in backend or frontend.
        logs                      Attaches logs to terminal.
        restart                   Restarts containers.
        run                       Runs an arbitrary command in a specified service (eg. 'run pgsqlserver build').
        start                     Start containers in detached mode.
        startwlogs                Start containers in detached mode, showing the logs.
        status                    Shows all containers, images, networks and volumes.
        stop                      Stops all containers.
    '''.format(
        volumes=red('and volumes'),
        images=red('removes all images'),
    ))
