# Base imports
from typing import (
    Dict,
    Generator,
    Optional,
    TextIO,
)


class BaseConfig:

    def __init__(self, dotenv_path: str) -> None:
        """Base constructor."""
        self._params = self._parse_dotenv_as_dict(dotenv_path)

        super(BaseConfig, self).__init__()

    @classmethod
    def _no_blank_lines(cls, file: TextIO) -> Generator[str, None, None]:
        """Yields non-blank lines from a text file."""
        for line in file:
            stripped = line.rstrip()
            if stripped:
                yield stripped

    @classmethod
    def _parse_dotenv_as_dict(cls, path: str) -> Optional[Dict[str, str]]:
        """Do the parsing of a dotenv file into a dictionary."""
        output: Dict[str, str] = {}

        with open(path, 'r') as dotenv_file:
            for line in cls._no_blank_lines(dotenv_file):
                if not line.startswith('#'):                                    # Ignoring commented lines
                    key, value = line.strip().replace('\n', '').split('=')      # Ignoring line breaks
                    output.update({key: value})

        return output
