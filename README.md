# udemy-pytest
Learning unit tests for Python with pytest

### Definition of tests
| Name | Definition | Complexity |
| ---- | ---------- | ---------- |
| Unit test | A test that checks a small bit of code, such a function or class, in isolation. | Low |
| Integration test | A test that checks a larger section of code, such as several classes or a subsystem. | Moderate |
| System test | A test that checks the entire system in an environment as close to the end-user as possible. | High |
| Functional test | A test that checks a single bit of functionality of a system. | Moderate |
| Subcutaneous test | A test that runs against an interface just below the end-user interface, for example against the API as opposed to the CLI (or GUI). This is a subset of functional testing.  | Moderate |

### Commonly used pytest CLI flags
| Flag | Description |
| ---- | ----------- |
| --help | Help documentation |
| -v, --verbose | Verbose traceback output |
| -collect-only | Only collect the tests, do not run them. Useful to: 1) check if your tests are recognized by pytest. 2) Identify single tests for isolated execution. |
| -k *expression* | Only run tests which match the given substring expression. |
| -m *expression* | Only run tests matching the given mark expression. Uses decorator style markings: @pytest.mark.<tag> Usefull when you have very large test suites. Allows execution to stagger from quick and small to large and slow. |
| -x | Exit on first failed test. Useful when you have very large test suites / execution times. Works well in conjuction with the -m flag. |
| --maxfail=*n* | Exit on *n^th* error. SImilar to -x flag. |
| --lf, --last-failed | Rerun only the tests that failed at the last run (or all if none failed). Useful when you have very large test suites. |
| --ff, --failed-first | Run all tests, but run the last failures first. |
| -l, --show-locals | Show local variables in traceback output. |
| --tb=no | Do not show traceback output. |
| --durations=*n* | Show top *n* test durations. Useful for large test suites / execution times |
| --version | Check pytest version |

## Finding pytest plugins
The pytest documentation: https://docs.pytest.org/en/latest/plugins.html 
Python home: https://pypi.python.org
GitHub: https://github.com/pytest-dev

### installing plugins
For example the code coverage plugin. From the terminal:

> pip install pytest-cov

## pytest configuration
| File | Description |
| ---- | ----------- |
| pytest.ini* | Initialization of pytest run. The primary configuration file to set default behavior |
| tox.ini* | Alternative to pytest.ini |
| setup.cfg* | Run the python setup.py test and have it run all tests. Alternative to pytest.ini |
| conftest.py | Hooks for functions and fixtures in the directory where conftest.py is located |
| \__init__.py | Allows for identical test filenames across directories |

*pytest looks for pytest.ini, tox.ini and setup.cfg and uses the first it finds.

## Installing the packages
* To do: install from github (clone)

Make sure pytest nor the project are installed globally. In the global env run:

> pytest --version
> tasks --version

If either shows up run:

> pip uninstall pytest
> pip uninstall tasks

Create a virtual environment:

> venv -m venv ~/.udemy-pytest 

Activate the virtual environment:

> source ~/.udemy-pytest/bin/activate

Install the project and pytest package in the virtual environment:

pip install pytest
pip install ./PyTest_Project1


## Section4 
Basic set-up to call pytest from a `test_foo.py` file.

## PyTest_Project1
Basic pytest syntax can be found in `tests/unit/test_task_fail.py`. This script shows failing tests. 

Somewhat more complex tests can be be found in `tests/unit/test_task.py`.

The use of fixtures and parameters is shown in `tests/unit/test_add_variety.py`. This includes support function for the test suite (*i.e.* equivalent), single parameters, and the set up of multiple parameters. 

## Pytest_Project4
A more detailed explanation of *markers* and *fixtures* to enable respectively selective testing and testing with multiple parameters at the same time.

## Pytest_Project5
The use of built-in fixtures, such as caching, tmpdir, and standard errors.

## Pytest_Project6
Creating plugins of your own.

## Pytest_Project7 - Configure tests

