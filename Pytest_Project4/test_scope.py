
import pytest

@pytest.fixture(scope='function')
def func_scope():
    '''
    some data
    '''

@pytest.fixture(scope='module')
def mod_scope():
    '''
    some data
    '''

@pytest.fixture(scope='session')
def session_scope():
    '''
    some data
    '''

@pytest.fixture(scope='class')
def class_scope():
    '''
    some data
    '''

def test_1(session_scope, mod_scope, func_scope):
    '''
    some data
    '''

def test_2(session_scope, mod_scope, func_scope):
    '''
    some data
    '''

@pytest.mark.usefixtures('class_scope')
class TestSomething():
    def test_3(self):
        '''
        some data
        '''

    def test_4(self):
        '''
        some data
        '''
