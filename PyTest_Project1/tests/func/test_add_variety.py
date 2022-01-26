from operator import eq
from pickletools import TAKEN_FROM_ARGUMENT1
import pytest
import tasks
from tasks import Task

def test_add_1():
    task = Task('run', 'James', True)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)

def equivalent(t1, t2):
    '''
    Assert that summary, owner and done parameters are the same for t1 and t2.

    Args:
    '''
    return (t1.summary == t2.summary and 
            t1.owner == t2.owner and
            t1.done == t2.done)

# Fixture
@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield 
    tasks.stop_tasks_db()

# Single parameter
@pytest.mark.parametrize('task', 
                        [Task('lift', done=True),
                        Task('swim', 'James'),
                        Task('run', 'James', True),
                        Task('play', 'Smith', False)])
def test_add_2(task):
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)

# Multiple parameters
@pytest.mark.parametrize('summary, owner, done',
                        [('lift', None, False),
                        ('swim', 'James', False),
                        ('run', 'James', True),
                        ('excercise', 'Smith', False)])
def test_add_3(summary, owner, done):
    task = Task(summary, owner, done)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)

# Multiple parameters (create a variable first)
tasks_to_try = (Task('lift', done=True),
                Task('swim', 'James'),
                Task('run', 'James', True),
                Task('play', 'Smith', False))

@pytest.mark.parametrize('task', tasks_to_try)
def test_add_4(task):
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)

# use list compherension
task_ids = ['Task({},{},{})'.format(t.summary, t.owner, t.done) for t in tasks_to_try] 

@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
def test_add_5(task):
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)

# use pytest.param
@pytest.mark.parametrize('task', [
    pytest.param(Task('set'), id='just summary'),
    pytest.param(Task('start', 'Pamela'), id='summary/owner'),
    pytest.param(Task('finish', 'Pamela', True), id='summary/owner/done')
    ])
def test_add_6(task):
    task_id = task.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)

# As a class
@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
class TestAdd():

    def test_equivalent(self, task):
        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        assert equivalent(t_from_db, task)

    def test_valid_id(self, task):
        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        assert t_from_db.id == task_id
        