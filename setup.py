import os
from codecs import open

from setuptools import setup, find_packages


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
VERSION = __import__('rpi_displays').__version__


with open(os.path.join(BASE_DIR, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


dev_require = [
    'pytest',
    'pytest-isort',
    'pytest-django',
    'pytest-cov',
    'pytest-flake8',
    'sphinx',
    'sphinx-rtd-theme',
    'factory-boy',
]


setup(
    name='rpi-displays',
    version=VERSION,
    description='Python library to put text/chars to several rpi displays.',
    long_description=long_description,
    url='https://github.com/deluge/rpi-displays',
    project_urls={
        'Bug Reports': 'https://github.com/deluge/rpi-displays/issues',
        'Source': 'https://github.com/deluge/rpi-displays',
    },
    author='Benjamin Banduhn',
    author_email='deluge@banduhn.com',
    packages=find_packages(exclude=['tests', 'tests.*', 'docs', 'examples*']),
    install_requires=[],
    extras_require={
        'dev': dev_require,
    },
    include_package_data=True,
    keywords='rpi displays raspberry pi',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
