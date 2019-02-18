# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='txb-api',
    version='1.0.0',
    packages=find_packages(),
    url='https://app.3xbit.com.br',
    license='',
    author='3xBit',
    author_email='drodrigues@3xbit.com.br',
    description='Software Development Kit',
    install_requires=[
        'requests'
    ],
)
