# Base imports
import os
from typing import Text


# File system related
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Project related
PROJECT_HOME = os.path.abspath(os.path.join(BASE_DIR, os.pardir, os.pardir))
PROJECT_PREFIX = "packiot-fsc-"

# Docker compose related
COMPOSE_FILE = os.path.join(PROJECT_HOME, "docker-compose.yaml")
COMPOSE_COMMAND = f'docker-compose -f \"{COMPOSE_FILE}\"'

# Dev environment related
POSTGRES_DOTENV = os.path.join(PROJECT_HOME, 'database/postgresql/docker/.pgsql.env')


def usage(text: Text) -> None:
    print(text)
