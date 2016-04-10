import os
from pip.req import parse_requirements
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


req_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
install_reqs = parse_requirements(req_path, session=False)

reqs = [str(ir.req) for ir in install_reqs]


setup(
    name = 'pydice',
    version ='0.1.0',
    author ='Justin Hammond',
    author_email ='justin@roaet.com',
    description ='python RPG Dice Parser and utilities',
    url ='https://github.com/roaet/pydice',
    packages = find_packages(),
    long_description =read('README.md'),
    install_requires=reqs,
    entry_points = {
        'console_scripts': [
            'pydice = pydice.client:main'
        ],
    }
)
