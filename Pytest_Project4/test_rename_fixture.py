import pytest

@pytest.fixture(name='myfixture')
def answer_to_the_question_of_the_universe():
    '''
    Hitch hiker
    '''
    return 42

def test_answer(myfixture):
    assert myfixture==42

