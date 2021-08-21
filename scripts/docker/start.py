# Base imports
from typing import Optional, List

# Project imports
from docker import common
from docker.run import run_with_compose


STARTWLOGS_USAGE_TEXT = '''
docker.start.startwlogs:
Starts a Docker Compose service and show the logs

Usage:
    $ ./scripts/devenv.py startwlogs [service_name]
    $ python /scripts/devenv.py startwlogs [service_name]
'''


def start(arguments: Optional[List[str]]) -> int:
    print(">>>>>>>>>>>>>>>>>>>> Starting Containers <<<<<<<<<<<<<<<<<<<<")

    command = ['up', '-d']

    if arguments:
        command += arguments

    return run_with_compose(command)


def startwlogs(arguments: List[str]) -> int:
    try:
        service_name = arguments[0]

        if not isinstance(service_name, str) or service_name == '':
            common.usage(STARTWLOGS_USAGE_TEXT)
            return -1

    except IndexError:
        print(f"You must inform one of the service names Listed in {common.COMPOSE_FILE}")
        common.usage(STARTWLOGS_USAGE_TEXT)
        return -1

    print(f">>>>>>>>>>>>>>>>>>>> Starting service {service_name} with logs <<<<<<<<<<<<<<<<<<<<")
    code = run_with_compose(['up', f'-d {service_name}'])
    code += run_with_compose(['logs', f'--follow {service_name}'])

    return code
