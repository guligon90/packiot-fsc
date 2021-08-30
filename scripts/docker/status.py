# Base imports
from typing import List

# Project imports
from docker import common
from docker.run import run_local


SUPPORTED_TYPES = [
    'container',
    'image',
    'volume',
    'network',
]


def status(arguments: List[str]) -> int:
    def command(_args, _type):
        base_cmd = f'docker {_type} ls'

        return f"{base_cmd} -f name={common.PROJECT_PREFIX} {' '.join(_args)}" \
            if _type != 'image' else base_cmd

    code: int = 0

    commands = {t: command(arguments, t) for t in SUPPORTED_TYPES}

    print(">>>>>>>>>>>>>>>>>>>> DOCKER STATUS <<<<<<<<<<<<<<<<<<<<")

    for _type, cmd in commands.items():
        print(f"\n\n{_type.upper()}S:")
        code += run_local(cmd)

    return code
