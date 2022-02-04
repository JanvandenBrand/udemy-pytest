
import pytest

def pytest_add_option(parser):
    group = parser.getgroup('nice')
    group.addoption("--nice", action='store_true',
    help="nice: turns a Failure into and OPPORTUNITY for improvement")

def pytest_report_header(config):
    if config.getoption('nice'):
        return "thanks for running the test"

def pytest_report_teststatus(report, config):
    if report.when == 'call':
        if report.failed and config.getoption('nice'):
            return (report.outcome, '0', 'OPPORTUNITY for improvement')


