from setuptools import setup
import re

def _get_version():
  """Extract version from package."""
  with open('syncconnect/__init__.py') as reader:
    match = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        reader.read(),
        re.MULTILINE
    )
    if match:
      return match.group(1)
    else:
      raise RuntimeError('Unable to extract version.')


def _get_long_description():
  """Get README contents."""
  with open('README.md') as reader:
    return reader.read()


setup(
    name='syncconnect',
    version=_get_version(),
    description='Sync Connect Python SDK',
    long_description=_get_long_description(),
    long_description_content_type='text/markdown',
    author='Ian White',
    author_email='ianjwhite99@gmail.com',
    packages=['syncconnect'],
    url='https://github.com/ianjwhite99/sync-connect',
    license='MIT',
    install_requires=[
        'requests'
    ]
)
