from wikit.languages import is_language

def test_is_language():
    assert is_language('da') == True
    assert is_language('ur') == True
    assert is_language('fr') == True
    assert is_language('abc') == False
    assert is_language('en') == True
    assert is_language('spanish') == False
    assert is_language('de') == True
    assert is_language('zh') == True
