import pytest
import tasks
from tasks import Task

@pytest.mark.skipif(tasks.__version__<'0.2.0', 
                    reason = 'higher version than 0.2.0 required')
def test_unique_id_1():
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2


def test_unique_id_2():
    task_ids = ['first', 'second', 'third'] 
    ids = [tasks.add(Task(id)) for id in task_ids]

    uid = tasks.unique_id()
    assert uid not in ids

@pytest.fixture(autouse=True)
def initialization_tasks_db(tmpdir):
    tasks.start_tasks_db(set(tmpdir), 'tiny')
    yield
    tasks.stop_tasks_db()



