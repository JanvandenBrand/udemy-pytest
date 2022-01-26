from tasks import Task

def test_asdict():
    t_task = Task('take action', 'Smith', True, 32)
    t_dict = t_task._asdict()
    expected = {'summary': 'take action',
                'owner': 'Smith',
                'done': True,
                'id': 32}
    assert t_dict == expected

def test_replace():
    t_before = Task('complete course', 'James', False)
    t_after = t_before._replace(id=9, done=True)
    t_expected = Task('completed course', 'James', True, 9)
    assert t_after == t_expected

def test_defaults():
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2

def test_number_access():
    t = Task('get cheese', 'James')
    assert t.summary == 'get cheese'
    assert t.owner == 'James'
    assert (t.done, t.id) == (False, None)

