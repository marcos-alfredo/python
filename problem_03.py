def fib(n):
    if n == 0:
        return None
    if n == 1:
        return 0
    if n == 2 or n == 3:
        return 1
    return fib(n-1) + fib(n-2)

def fibi(n):
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a+b
    return a

def test_0():
    assert fibi(0) == 0

def test_1():
    assert fibi(1) == 0

def test_2():
    assert fibi(2) == 1

def test_3():
    assert fibi(3) == 1

def test_4():
    assert fibi(4) == 2

def test_10():
    assert fibi(10) == 34

def test_20():
    assert fibi(20) == 4181

def test_30():
    assert fibi(30) == 514229

def test_35():
    assert fibi(35) == 5702887
