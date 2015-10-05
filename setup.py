from setuptools import setup
from pip.req import parse_requirements as parse

requirements = map(lambda r: str(r.req), parse('requirements.txt'))
description = ('Speakerfight is an arena where the Speakers can '
               'fight each other and the people choose who wins.')

setup(
    name='Speakerfight',
    description=description,
    author='Luan Fonseca',
    author_email='luanfonceca@gmail.com',
    url='http://speakerfight.com',
    install_requires=requirements,
)
