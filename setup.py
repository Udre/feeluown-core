#!/usr/bin/env python3

from setuptools import setup

import fuocore


setup(
    name='fuocore',
    version=fuocore.__version__,
    description='feeluown core',
    author='Cosven',
    author_email='cosven.yin@gmail.com',
    py_modules=['mpv'],
    packages=[
        'fuocore',
        'fuocore.third_party',
        'fuocore.third_party.netease'
        ],
    package_data={
        '': []
        },
    url='https://github.com/cosven/feeluown-core',
    keywords=['media', 'player', 'api'],
    classifiers=(
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
        ),
    install_requires=[
        'pycrypto>=2.6.1',
        'requests>=2.13.0',
        'beautifulsoup4>=4.5.3',
        'marshmallow>=2.13.5',
        'april>=0.0.1a4',
        'aiozmq',
        'msgpack-python',
        'mutagen>=1.37',
        'python-Levenshtein>=0.12.0',
        ],
    setup_requires=['pytest-runner'],
    tests_require=[
        'pytest',
        'mock'
    ],
    entry_points={
        'console_scripts': []
        },
    )
