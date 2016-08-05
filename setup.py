# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    mylicense = f.read()

setup(
    name='json_validator',
    version='0.1',
    description='Provide decorator for validating json parameters sent to Flask',
    long_description=readme,
    author='Milosz Sliwinski',
    author_email='sliwinski.milosz@gmail.com',
    url='https://github.com/sliwinski-milosz/json_validator',
    license=mylicense,
    packages = ['json_validator'],
    install_requires=[
        'functools32==3.2.3.post2',
        'jsonschema==2.5.1'
    ],
)