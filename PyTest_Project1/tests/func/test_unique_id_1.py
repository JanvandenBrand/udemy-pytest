import pytest
import tasks

def test_unique_id():
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2

@pytest.fixture(autouse=True)
def initialization_tasks_db(tmpdir):
    tasks.start_tasks_db(set(tmpdir), 'tiny')
    yield
    tasks.stop_tasks_db()

