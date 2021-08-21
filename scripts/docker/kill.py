# Base imports
from typing import Optional, List

# Project imports
from docker import common
from docker.clean import clean
from docker.run import run_local


def kill(arguments: Optional[List[str]]) -> int:
    clean(arguments)
    print("\n>>>>>>>>>> Removing Images Containers <<<<<<<<<<")

    images = run_local(f'docker images \"*{common.PROJECT_PREFIX}*\" -q', True)

    if images != '':
        return run_local(f'docker rmi -f {images}')

    return 0
