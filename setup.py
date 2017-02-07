# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    mylicense = f.read()

setup(
    name='json_validator',
    version='1.0',
    description='''Provide decorator for validating json parameters passed to function. '''
                '''Can be used for validation of json parameters sent to Flask.''',
    long_description=readme,
    author='Milosz Sliwinski',
    author_email='sliwinski.milosz@gmail.com',
    url='https://github.com/sliwinski-milosz/json_validator',
    license=mylicense,
    packages=['json_validator'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'jsonschema==2.5.1'
    ],
)
