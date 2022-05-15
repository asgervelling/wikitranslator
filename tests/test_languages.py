from wikit.languages import is_language


def test_is_language():
    assert is_language('da')
    assert is_language('ur')
    assert is_language('fr')
    assert not is_language('abc')
    assert is_language('en')
    assert not is_language('spanish')
    assert is_language('de')
    assert is_language('zh')
