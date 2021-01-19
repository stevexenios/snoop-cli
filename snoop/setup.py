"""Packaging settings."""
from setuptools import setup, find_packages
from os.path import abspath, dirname, join


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()


setup(
    name='snoop',
    version='1.0',
    description = 'A command line program developed using Python (and click).',
    packages=find_packages(),
    long_description = long_description,
    url = 'https://github.com/stevexenios/rover',
    author = 'Steve Mwangi',
    author_email = 'stevexenios@gmail.com',
    license = 'UNLICENSE',
    classifiers = [
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords = 'cli',
    install_requires=[
        'Click',
        ],
    entry_points='''
        [console_scripts]
        snoop=snoop:cli
    ''',
)