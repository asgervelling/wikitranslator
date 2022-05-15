from wikit.translations import clean_title, translate


def test_clean_title():
    assert clean_title('<title>Linear Algebra - Wikipedia</title>') \
        == 'Linear Algebra'
    assert clean_title('<title>Álgebra lineal - Wikipedia, la enciclopedia libre</title>') \
        == 'Álgebra lineal'
    assert clean_title('<title>线性代数 - 维基百科，自由的百科全书</title>') \
        == '线性代数'


def test_translate():
    assert translate('lineær algebra', 'da', 'de') \
        == 'Lineare Algebra'

    assert translate('Lineare Algebra', 'de', 'zh') \
        == '线性代数'

    assert translate('线性代数', 'zh', 'tr') \
        == 'Lineer cebir'

    assert translate('Dampmaskine', 'da', 'de') \
        == 'Dampfmaschine'

    assert translate('Dampmaskine', 'da', 'ur') \
        == 'دخانی انجن'
