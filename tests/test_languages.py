from wikit.languages import get_language_code, is_language_code, is_language


def test_is_language_code():
    assert is_language_code('da')
    assert is_language_code('ur')
    assert is_language_code('fr')
    assert not is_language_code('abc')
    assert is_language_code('en')
    assert not is_language_code('spanish')
    assert is_language_code('de')
    assert is_language_code('zh')


def test_is_language():
    assert not is_language('aslkdj')
    assert is_language('en')
    assert is_language('eng')
    assert is_language('english')
    assert is_language(' english  ')
    assert is_language(' ENGLISH ')


def test_get_language_code():
    assert get_language_code(' english') == 'en'
    assert get_language_code('england') is None
    assert get_language_code('deu') == 'de'
    assert get_language_code('Deutsch') == 'de'
