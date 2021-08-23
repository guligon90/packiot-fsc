#!/usr/bin/python3

# Base imports
import sys
from typing import Optional, List

# Project imports
from docker.build import build
from docker.clean import clean
from docker.code import analyze
from docker.db import db_action
from docker.dev import dev
from docker.kill import kill
from docker.logs import logs
from docker.restart import restart
from docker.run import run_with_compose
from docker.start import start, startwlogs
from docker.status import status
from docker.stop import stop
from docker.usage import usage


def argument_to_command(arguments: Optional[List[str]]) -> None:
    commands = {
        "build": build,
        "clean": clean,
        "code": analyze,
        "db": db_action,
        "dev": dev,
        "kill": kill,
        "logs": logs,
        "restart": restart,
        "run": run_with_compose,
        "start": start,
        "startwlogs": startwlogs,
        "status": status,
        "stop": stop,
    }

    ret = 0

    if arguments is not None:
        command = commands.get(arguments[0], usage)
        ret = command(arguments[1:])

    sys.exit(ret)


def main() -> None:
    arguments = sys.argv[1:]

    if not arguments:
        usage([])
        return

    try:
        argument_to_command(arguments)
    except KeyboardInterrupt:
        pass

    return


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as exc:
        print(f'{exc.__class__.__name__}: {str(exc)}')
        sys.exit(-1)
