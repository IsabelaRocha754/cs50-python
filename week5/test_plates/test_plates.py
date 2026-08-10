from plates import is_valid

def test_valid_plates():
    assert is_valid('HELLO') == True
    assert is_valid('cs50') == True

def test_length():
    assert is_valid('H') == False
    assert is_valid('ABCDEFG') == False

def test_beginning_letters():
    assert is_valid('50') == False

def test_number_placement():
    assert is_valid('AB1C') == False

def test_zero_placement():
    assert is_valid('cs05') == False

def test_alphanumeric():
    assert is_valid('HELLO, WORLD') == False
    assert is_valid('AB!CD') == False
