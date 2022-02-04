from setuptools import setup

setup(
    name='pytest-nice',
    version='0.0.900',
    description='A plugin to make the FAILURE into an OPPORTUNITY',
    py_modules=['pytest_nice'],
    install_requires=['pytest'],
    entry_points={'pytest11': ['nice=pytest_nice',], },
    )
