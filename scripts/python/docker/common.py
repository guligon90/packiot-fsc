# Base imports
import os
from enum import Enum
from functools import reduce
from typing import Text, Union


# File system related
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Project related
PROJECT_HOME = os.path.abspath(os.path.join(BASE_DIR, os.pardir, os.pardir))
PROJECT_PREFIX = "packiot-fsc-"

# Docker compose related
COMPOSE_FILE = os.path.join(PROJECT_HOME, "../docker-compose.yaml")
COMPOSE_COMMAND = f'docker-compose -f \"{COMPOSE_FILE}\"'


def usage(text: Text) -> None:
    print(text)


class DatabaseConfig(Enum):
    HOST = os.getenv('DB_HOST', None)
    NAME = os.getenv('DB_NAME', None)
    PASSWORD = os.getenv('DB_PASSWORD', None)
    PORT = os.getenv('DB_PORT', None)
    USER = os.getenv('DB_USER', None)

    @classmethod
    def has_credentials(cls):
        """Checks if all credentials in the enum were set."""
        def condition(value: Union[str, int]) -> bool:
            """Auxiliary closured function, implementing the checking."""
            return isinstance(value, (int, str)) and value not in ['', None]

        return reduce(
            lambda x, y: condition(x) and condition(y),     # Pairwise verification
            [credential.value for credential in cls],       # Credentials' values
            False                                           # Default value of the reducer
        )


def must_have_db_credentials(func):
    """Decorator that restricts access to DB actions if the credentials were not set."""
    def wrapper(*args, **kwargs):
        print(DatabaseConfig.has_credentials())

        if not DatabaseConfig.has_credentials():
            print('The DB credentials were not set in the dev environment')
            return -1

        return func(*args, **kwargs)

    return wrapper
