# to import my environment as a package - setup is used

from setuptools import setup, find_packages
from typing import List


def getrequirements(path: str) -> List[str]:
    with open(path) as func:
        requirements = [
            line.strip()
            for line in func
            if line.strip() and not line.strip().startswith('-e') and not line.strip().startswith('#')
        ]
    return requirements

setup(
    name='my_newproject',
    version='0.1.0',
    author = 'Aniruddhan Narasimhan',
    author_email = 'anarasim@umd.edu',
    packages=find_packages(),
    install_requires=getrequirements('requirements.txt')

)