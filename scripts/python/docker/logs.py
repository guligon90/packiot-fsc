# Base imports
from typing import List

# Project imports
from docker.run import run_with_compose


def logs(arguments: List[str]) -> int:
    print(">>>>>>>>>>>>>>>>>>>> Logs <<<<<<<<<<<<<<<<<<<<")

    return run_with_compose(['logs', '--follow'] + arguments)
