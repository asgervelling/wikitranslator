from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup, element
from typing import Union

"""
Translate a word that might not be found in a dictionary,
using Wikipedia article names..
Language names follow ISO 639-1: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

Translation from Danish to English:

>>> wikit --da/en "lineær algebra"
Request to danish wikipedia for "Lineær algebra"
Request english article
Return the title:
-> "Linear algebra"

"""


""" Case 1:
        from_lang:   da
        to_lang:     en 
        term:   "Lineær algebra"

        Expected result: "Linear algebra"

    Case 2:
        from_lang:   en
        to_lang:     da
        term:   Invertible matrix

        Expected result: None
        (Article does not exist in Danish)
"""


def make_request(url) -> requests.Response:
    return requests.get(url)


def translate(from_lang, to_lang, term):
    from_url = make_url(from_lang, term)
    from_article = BeautifulSoup(make_request(from_url).content, 'html.parser')
    for lang, link in language_links(from_article):
        if lang == to_lang:
            soup = BeautifulSoup(make_request(link).content, 'html.parser')
            title = clean_title(soup.title)
            return title
    

def language_links(article: BeautifulSoup):
    links = [(el.get('lang'), el.get('href')) for el in article.select('li.interlanguage-link > a')]
    return links


def clean_title(title: Union[element.Tag, str]) -> str:
    """ '<title>Lineær Algebra - Wikipedia</title>' -> 'Lineær Algebra' """
    dirty_string = title
    if type(title) == element.Tag:
        dirty_string = title.text

    s0 = dirty_string.replace('—', '-')
    s1 = s0.replace('–', '-')
    s2 = s1.replace('<title>', '')
    s3 = s2.replace('</title>', '')
    
    parts = s3.split(sep='-')
    title = parts[0]
    print(title)
    return title.strip()

def make_url(lang, term):
    return f'https://{lang}.wikipedia.org/wiki/{term}'


print(translate('da', 'de', 'lineær algebra'))