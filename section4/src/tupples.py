from collections import namedtuple

dinner = namedtuple('Dinner', 
['food', 'cook', 'ready', 'id'])
dinner.__new__.__defaults__ = (None, None, False, None)

def test_defaults():
    t1 = dinner()
    t2 = dinner(None, None, False, None)
    assert t1 == t2

def test_num_access():
    t = dinner('potatoes', 'Sam')
    assert t.food == 'potatoes'
    assert t.cook == 'Sam'
    assert (t.ready, t.id) == (False, None)

def test_asdict():
    t_dinner = dinner('potatoes', 'Peter', True, 34)
    t_dict = t_dinner._asdict()
    expected = {'food': 'potatoes',
                'cook': 'Peter',
                'ready': True,
                'id': 34}
    assert t_dict == expected

def test_replace():
    t_before = dinner('meat', 'Sam', False)
    t_after = t_before._replace(id=10, ready=True)
    t_expected = dinner('meat', 'Sam', True, 10)
    assert t_after == t_expected
