NAME = 'aocpaiv'
VERSION = '0.1.2020'
DESCRIPTION = 'paiv helper library for solving Advent of Code'
AUTHOR = 'Pavel paiv Ivashkov'
LICENSE = 'MIT'
URL = 'https://github.com/paiv/'


from setuptools import setup

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    license=LICENSE,
    url=URL,

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],

    packages=['aocpaiv'],

    python_requires='>=3.6',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
