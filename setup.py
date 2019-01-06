from setuptools import setup, find_packages

long_description = open('README.md').read()

setup(
  name='Discord Webhooks',
  version='1.0.4',
  py_modules=['discord_webhooks'],
  url='https://github.com/JamesIves/discord-webhooks',
  author='James Ives',
  author_email='iam@jamesiv.es',
  description='Easy to use module for Python which allows for sending of webhooks to a Discord server.',
  long_description=long_description,
  license='MIT',
  install_requires=[
    'requests==2.21.0'
  ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Environment :: Other Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
  ],
)