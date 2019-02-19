# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='txb-api',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/3xbit/python-txb-api',
    license='MIT License',
    author='3xBit',
    author_email='drodrigues@3xbit.com.br',
    description='Python wrapper for 3xBit API',
    install_requires=[
        'requests'
    ],
)
