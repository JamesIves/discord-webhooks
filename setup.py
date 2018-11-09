from setuptools import setup, find_packages

long_description = open('README.md').read()

setup(
  name='Discord Webhooks',
  version='1.0.1',
  packages=find_packages(exclude=['tests', 'tests.*']),
  url='https://github.com/JamesIves/discord-webhooks',
  author='James Ives',
  author_email='iam@jamesiv.es',
  description='Easy to use package for Python which allows for sending of webhooks to a Discord server.',
  long_description=long_description,
  license='MIT',
  install_requires=[
    'requests==2.20.0'
  ],
  classifiers=[
    'Programming Language :: Python :: 3'
  ],
)