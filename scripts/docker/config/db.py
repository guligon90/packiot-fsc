# Project imports
from docker.common import POSTGRES_DOTENV
from docker.config.base import BaseConfig


class PostgreSQLConfig(BaseConfig):

    # Mapping between internal config and .env values (vary between DB platforms)
    _credentials_mapping = [
        ('NAME', 'DATABASE'),
        ('PORT', 'PORT'),
        ('HOST', 'HOST'),
        ('USERNAME', 'POSTGRES_USER'),
        ('PASSWORD', 'POSTGRES_PASSWORD'),
    ]

    def __init__(self, dotenv_path: str = POSTGRES_DOTENV) -> None:
        """Constructor."""
        super(PostgreSQLConfig, self).__init__(dotenv_path)

        for item in self._credentials_mapping:
            if self._params:
                setattr(self, item[0], self._params[item[1]])

    def has_credentials(self):
        """Check if the DB credentials were set."""
        credentials = [
            getattr(self, item[0]) for item in self._credentials_mapping
        ]

        return all(credentials)     # Logical 'and' in all list

    def must_have_db_credentials(self, func):
        """Decorator that restricts access to DB actions if the credentials were not set."""
        def wrapper(*args, **kwargs):
            if not self.has_credentials():
                print('The DB credentials were not set in the dev environment')
                return -1

            return func(*args, **kwargs)

        return wrapper


DBCONFIG = PostgreSQLConfig()
