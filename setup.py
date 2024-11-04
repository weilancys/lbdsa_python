from setuptools import setup

with open('README.md') as f:
    desp = f.read()

setup(
    name='lbdsa',
    version='0.0.1',
    packages=['lbdsa', ],
    description=desp
)