# Base imports
from typing import List

# Project imports
from docker.common import usage
from docker.run import run_local


# Gives flexibility to add linting to more sections of the project
SUPPORTED_PARAMS = {
    'python': {
        'lint': 'prospector',
    },
    'sql': {
        'fix': 'sqlfluff fix --force',
        'lint': 'sqlfluff lint --ignore=parsing',
    },
}


ANALYZE_USAGE_TEXT = '''
docker.code.analyze:
Performs the linting or fixing of the code base.

Usage:
    $ ./scripts/devenv.py code [language] [action]
    $ python /scripts/devenv.py code [language] [action]

Where:
    language: python | sql
    action: fix | lint
'''


def analyze(arguments: List[str]) -> int:
    try:
        language = arguments[0]
        action = arguments[1]
    except IndexError:
        usage(ANALYZE_USAGE_TEXT)
        return -1

    print(f'>>>>>>>>> Running {language} {action} <<<<<<<<<<')

    actions = SUPPORTED_PARAMS.get(language, {})
    command = actions.get(action, '')

    if command != '':
        return run_local(f"{command} {' '.join(arguments[2:])}")

    usage(ANALYZE_USAGE_TEXT)
    return -1
