# Base imports
from typing import Optional, List

# Project imports
from docker import common
from docker.run import run_local


def clean(_: Optional[List[str]]):
    code: int = 0

    print(">>>>>>>>>> Removing Docker Containers <<<<<<<<<<")
    containers = run_local(f'docker ps -a -q -f \"name={common.PROJECT_PREFIX}\"', True)

    if containers != '':
        code += run_local(f'docker rm -f {containers}')

    print("\n>>>>>>>>>> Removing Docker Volumes <<<<<<<<<<")
    volume_prefix = common.PROJECT_PREFIX.replace('-', '_')  # docker volumes can't use '-'
    volumes = run_local(f'docker volume ls -q -f \"name={volume_prefix}\" -f \"dangling=true\"', True)

    if volumes != '':
        code += run_local(f'docker volume rm {volumes}')

    print("\n>>>>>>>>>> Removing Docker Networks <<<<<<<<<<")
    networks = run_local(f'docker network ls -q -f \"name={common.PROJECT_PREFIX}\"', True)

    if networks != '':
        clean_command = f'docker network rm {networks}'
        code += run_local(clean_command)

    return code
