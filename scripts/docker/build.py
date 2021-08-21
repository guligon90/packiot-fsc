# Base imports
from typing import List

# Project imports
from docker.run import run_with_compose


def build(arguments: List[str]) -> int:
    print(">>>>>>>>>>>>>>>>>>>> Building <<<<<<<<<<<<<<<<<<<<")

    return run_with_compose(['build', '--pull'] + arguments)
