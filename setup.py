import codecs
import os
import sys

from setuptools import setup, find_packages


VERSION = __import__('rpi_displays').__version__


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    print('You probably want to also tag the version now:')
    print('  git tag -a %s -m "version %s"' % (VERSION, VERSION))
    print('  git push --tags')
    sys.exit()


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


test_requirements = [
    'tox',
    'tox-pyenv',
    'mock',
    'factory-boy',
    'pydocstyle',
    'pytest',
    'pytest-cov',
    'pytest-flakes',
    'pytest-pep8',
    'pytest-isort',
]


setup(
    name='rpi-displays',
    version=VERSION,
    url='https://github.com/deluge/rpi-displays',
    author='Benjamin Banduhn',
    author_email='deluge@banduhn.com',
    description='Python library to put text/chars to several rpi displays.',
    long_description=read('README.rst'),
    license='GNU GENERAL PUBLIC',
    packages=find_packages(exclude=['examples*', 'tests*']),
    include_package_data=True,
    install_requires=[],
    extras_require={
        'tests': test_requirements,
        'docs': ['sphinx>=1.4,<1.5'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
