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
| -k <expression> | Only run tests which match the given substring expression. |
| -m <expression> | Only run tests matching the given mark expression. Uses decorator style markings: @pytest.mark.<tag> Usefull when you have very large test suites. Allows execution to stagger from quick and small to large and slow. |
| -x | Exit on first failed test. Useful when you have very large test suites / execution times. Works well in conjuction with the -m flag. |
| --maxfail=<n> | Exit on <n-th> error. SImilar to -x flag. |
| --lf, --last-failed | Rerun only the tests that failed at the last run (or all if none failed). Useful when you have very large test suites. |
| --ff, --failed-first | Run all tests, but run the last failures first. |
|-l, --show-locals | Show local variables in traceback output. |
| --tb=no | Do not show traceback output. |
| --durations=<n> | Show top n test durations. Useful for large test suites / execution times |
|--version | Check pytest version |

## Section4 
Basic set-up to call pytest from a test_foo.py file.

## PyTest_Project1
Basic pytest syntax can be found in `tests/unit/test_task_fail.py`. This script shows (obviously) failing tests. 

Somewhat more complext tests can be be found in `tests/unit/test_task.py`.

The use of fixtures and parameters is shown in `tests/unit/test_add_variety.py`. This includes support function for the test suite (*i.e.* equivalent), single parameters, and the set up of multiple parameters. 



