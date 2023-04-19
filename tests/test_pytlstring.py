from pytlstring.main import tlstring

def test_1():
    aa, ab, bb = 5, 0, 2
    exp = {'AABBAABBAA'}
    res = tlstring(aa, ab, bb)
    assert res in exp

def test_2():
    aa, ab, bb = 1, 2, 1
    exp = {'BBABABAA', 'ABAABBAB', 'ABABAABB', 'AABBABAB'}
    res = tlstring(aa, ab, bb)
    assert res in exp

def test_3():
    aa, ab, bb = 0, 2, 0
    exp = {'ABAB'}
    res = tlstring(aa, ab, bb)
    assert res in exp

def test_4():
    aa, ab, bb = 0, 0, 10
    exp = {'BB'}
    res = tlstring(aa, ab, bb)
    assert res in exp
