from twttr import shorten

def test_twttr():
    assert shorten('twitter') == 'twttr'
    assert shorten('bloomie') == 'blm'

def test_punctuation():
    assert shorten('hello!') == 'hll!'

def test_numbers():
    assert shorten('h3llo') == 'h3ll'

def test_capitalized():
    assert shorten('HELLO') == 'HLL'
