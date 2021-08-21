# Base imports
from typing import List

# Project imports
from docker.run import run_with_compose


def stop(arguments: List[str]) -> int:
    print(">>>>>>>>>>>>>>>>>>>> Stopping services <<<<<<<<<<<<<<<<<<<<")

    return run_with_compose(['stop'] + arguments)
