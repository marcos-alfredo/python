def mix_lists (list1, list2):
    result_list = []
    while len(list1) > 0 or len(list2) > 0:
        if len(list1) > 0:
            result_list.append(list1.pop(0))
        if len(list2) > 0:
            result_list.append(list2.pop(0))
    return result_list

def test_both_empty():
    result = mix_lists([], [])
    assert result == []

def test_first_empty():
    result = mix_lists([], ['a', 'b', 'c'])
    assert result == ['a', 'b', 'c']

def test_second_empty():
    result = mix_lists(['a', 'b', 'c'], [])
    assert result == ['a', 'b', 'c']

def test_same_size():
    result = mix_lists(['a', 'b', 'c'], [1, 2, 3])
    assert result == ['a', 1, 'b', 2, 'c', 3]

def test_different_size():
    result = mix_lists(['a', 'b', 'c', 'd'], [1, 2, 3])
    assert result == ['a', 1, 'b', 2, 'c', 3, 'd']
