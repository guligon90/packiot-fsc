# Base imports
from typing import List

# Project imports
from docker.run import run_with_compose


def dev(arguments: List[str]) -> int:
    print(">>>>>>>>>>>>>>>>>>>> Starting Containers <<<<<<<<<<<<<<<<<<<<")

    return run_with_compose(['up'] + arguments)
