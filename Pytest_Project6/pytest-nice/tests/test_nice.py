from cgitb import reset
from random import sample
from unittest import result
import pytest

def test_pass_fail(testdir):
    '''
    Create a tempdir to store test results
    '''
    testdir.makepyfile(
        '''
        def test_pass():
            assert 1 == 1
            
        def test_fail():
            assert 2 == 1
        ''')

    result = testdir.runpytest()

    result.stdout.fnmatch_lines([
        '*.F*',
    ])
    
    # Did any test fail?
    # . for PASS
    # 1 for FAILED
    assert result.ret == 1

@pytest.fixture()
def sample_test(testdir):
    testdir.makepyfile(
        '''
        def test_pass():
            assert 1 == 1
            
        def test_fail():
            assert 2 == 1
        '''
    )

    return testdir

def test_with_nice(sample_test):
    result = sample_test.runpytest('--nice')
    result.stdout.fnmatch_lines(['*.0*'])
    assert result.ret == 1

def test_with_nice_verbose(sample_test):
    result = sample_test.runpytest('-v', '--nice')
    result.stdout.fnmatch_lines(['*::test_fail OPPORTUNITY for improvement'])
    assert result.ret == 1

def test_not_nice_verbose(sample_test):
    result = sample_test.runpytest('-v')
    result.stdout.fnmatch_lines(['*test_fail FAILED'])
    assert result.ret == 1

def test_header(sample_test):
    result=sample_test.runpytest('--nice')
    result.stdout.fnmatch_lines(['thanks for running the test'])

def test_header_not_nice(sample_test):
    result = sample_test.runpytest()
    thanks_message = 'thanks for running the test'
    assert thanks_message not in result.stdout.str()

def test_help_message(testdir):
    result = testdir.runpytest('--help')
    result.stdout.fnmatch_lines(['nice:', '*--nice*nice: turns a Failure into and OPPORTUNITY for improvement'])
