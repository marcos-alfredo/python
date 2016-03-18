def sum_for (numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total

def sum_while(numbers):
    total = 0
    while len(numbers) > 0:
        total = total + numbers.pop()
    return total

def sum_recursion(numbers):
    if len(numbers) == 0:
        return 0
    elif len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + sum_recursion(numbers[1:])

def test_sum_for_001():
    result = sum_for([1, 2, 3])
    assert result == 6

def test_sum_for_002():
    result = sum_for([-1, 2, 3, -2])
    assert result == 2

def test_sum_for_003():
    result = sum_for([5])
    assert result == 5

def test_sum_for_004():
    result = sum_for([])
    assert result == 0

def test_while_for_001():
    result = sum_while([1, 2, 3])
    assert result == 6

def test_while_for_002():
    result = sum_while([-1, 2, 3, -2])
    assert result == 2

def test_while_for_003():
    result = sum_while([5])
    assert result == 5

def test_while_for_004():
    result = sum_while([])
    assert result == 0

def test_recursive_for_001():
    result = sum_recursion([1, 2, 3])
    assert result == 6

def test_recursive_for_002():
    result = sum_recursion([-1, 2, 3, -2])
    assert result == 2

def test_recursive_for_003():
    result = sum_recursion([5])
    assert result == 5

def test_recursive_for_004():
    result = sum_recursion([])
    assert result == 0
