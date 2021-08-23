# Base imports
import subprocess
from typing import List, Optional, Union

# Project imports
from docker import common


def run_with_compose(
    arguments: List[str],
    deps: Optional[bool] = False,
    inside_container: Optional[bool] = False
) -> int:
    """Runs a command, using the project's Docker Compose .yaml file."""
    if inside_container:
        compose_arguments = 'run --rm' if deps else 'run --rm --no-deps'
        command = f"{common.COMPOSE_COMMAND} {compose_arguments} {' '.join(arguments)}"
    else:
        command = f"{common.COMPOSE_COMMAND} {' '.join(arguments)}"

    print(command)
    return subprocess.call(command, shell=True)


def run_local(command: str, str_output: Optional[bool] = False) -> Union[int, str]:
    """Runs a command locally and captures output."""
    print(command)

    if str_output:
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            universal_newlines=True
        )

        return process.communicate()[0].replace("\n", " ")

    return subprocess.call(command, shell=True)
