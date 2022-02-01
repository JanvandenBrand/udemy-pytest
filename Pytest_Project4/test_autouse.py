
import pytest
import time

@pytest.fixture(autouse=True, scope='session')
def footer_session_scope():
    '''
    Report the end of test session
    '''
    yield

    now = time.time()
    print('--------')
    print('finished: {}'.format(time.strftime('%d-%m-%Y: %X', time.localtime(now))))
    print('--------')

@pytest.fixture(autouse=True)
def footer_function_scope():
    '''
    Report the duration that each test took
    '''
    start = time.time()

    yield

    stop = time.time()
    delta = stop - start
    print('\ntest duration: {:0.3} seconds'.format(delta))

def test_1():
    time.sleep(1)

def test_2():
    time.sleep(1.23)



