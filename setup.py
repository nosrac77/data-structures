"""This file contains setup information for multiple data-structures."""

from setuptools import setup

setup(
    name='Data-Structures',
    description='Contains setup for Data-Structues repository.',
    author='Chelsea and Carson',
    author_email='carson.newton@outlook.com',
    package_dir={'': 'src'},
    py_modules=[],
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov']},
)
