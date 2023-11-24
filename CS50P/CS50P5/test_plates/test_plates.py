from plates import is_valid

def test_s():
    assert is_valid("123") == False
    assert is_valid("225") == False
    assert is_valid("AA2") == True

def test_m():
    assert is_valid("C") == False
    assert is_valid("ABCDEFG") == False
    assert is_valid("ABCDEF") == True

def test_n():
    assert is_valid("123456") == False
    assert is_valid("123ABC") == False
    assert is_valid("XXX012") == False
    assert is_valid("AB12C3") == False
    assert is_valid("AB12BB") == False
    assert is_valid("ABC678") == True

def test_sym():
    assert is_valid("ABC?!-") == False
    assert is_valid(". 12[]") == False
    assert is_valid("/B^D3*") == False