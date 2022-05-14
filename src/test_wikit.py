from wikit import clean_title, translate
from bs4 import BeautifulSoup, element

def test_clean_title():
    assert clean_title('<title>Linear Algebra - Wikipedia</title>') \
        == 'Linear Algebra'
    assert clean_title('<title>Álgebra lineal - Wikipedia, la enciclopedia libre</title>') \
        == 'Álgebra lineal'
    assert clean_title('<title>线性代数 - 维基百科，自由的百科全书</title>') \
        == '线性代数'


def test_translate():
    assert translate('da', 'de', 'lineær algebra') \
        == 'Lineare Algebra'

    assert translate('de', 'zh', 'Lineare Algebra') \
        == '线性代数'

    assert translate('zh', 'tr', '线性代数') \
        == 'Lineer cebir'
        