from tasks import Task

def test_task_equality():
    t1 = Task('sit there', 'James')
    t2 = Task('do something', 'Smith')
    assert t1 == t2

def  test_dict_equality():
    t1_dict = Task('make sandwich', 'Smith')._as_dict()
    t2_dict = Task('make sandwich', 'Smit')._asdict()
    assert t1_dict == t2_dict

