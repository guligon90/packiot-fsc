# Base imports
from typing import List

# Project imports
from docker.run import run_with_compose


def restart(arguments: List[str]) -> int:
    print(">>>>>>>>>>>>>>>>>>>> Restarting Containers <<<<<<<<<<<<<<<<<<<<")

    return run_with_compose(['restart'] + arguments)
