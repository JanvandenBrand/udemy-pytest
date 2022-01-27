
import pytest
import tasks
from tasks import Task

@pytest.mark.skip(reason='misunderstood the API')
def test_unique_id_1():
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2

list_ids = ['one', 'two', 'three']
def test_unique_id_2():
    ids = [tasks.add(Task(id)) for id in list_ids]
    
    uid = tasks.unique_id()
    assert uid not in ids

@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield
    tasks.stop_tasks_db()

    