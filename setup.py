from os.path import dirname, isdir, join
from setuptools import setup
import subprocess
import os
import re


def _get_version():
    """Extract version from git."""
    version_re = re.compile('^Version: (.+)$', re.M)
    d = dirname(__file__)

    if isdir(join(d, '.git')):
        # Get the version using "git describe".
        cmd = 'git describe --tags --match [0-9]*'.split()

        try:
            version = subprocess.check_output(cmd).decode().strip()
        except subprocess.CalledProcessError:
            print('Unable to get version number from git tags')
            exit(1)

        if '-' in version:
            version = '.post'.join(version.split('-')[:2])

        with open(os.devnull, 'w') as fd_devnull:
            subprocess.call(['git', 'status'],
                            stdout=fd_devnull, stderr=fd_devnull)

        cmd = 'git diff-index --name-only HEAD'.split()

        try:
            dirty = subprocess.check_output(cmd).decode().strip()
        except subprocess.CalledProcessError:
            print('Unable to get git index status')
            exit(1)

        if dirty != '':
            version += '.dev1'

    else:
        # Extract the version from the PKG-INFO file.
        with open(join(d, 'PKG-INFO')) as f:
            version = version_re.search(f.read()).group(1)

    return version


def _get_long_description():
    """Get README contents."""
    with open('README.md') as reader:
        return reader.read()


setup(
    name='connectedcar',
    version=_get_version(),
    description='ConnectedCar SDK',
    long_description=_get_long_description(),
    long_description_content_type='text/markdown',
    author='Ian White',
    author_email='iwhite99@protonmail.com',
    packages=['connectedcar'],
    url='https://github.com/ianjwhite99/connected-car-python-sdk',
    license='MIT',
    install_requires=[
        'requests'
    ],
    extras_require={
        "dev": [
            "coverage",
            "nose",
            "responses",
            "pylint",
            "python-dotenv",
            "requests"
        ]
    },
)
