![Tests](https://github.com/asgervelling/wikitranslator/actions/workflows/tests.yml/badge.svg)

# Wikitranslator

## Translate using Wikipedia

Typically when I can't find a translation in a dictionary, I find its article on Wikipedia in the language I want to translate from, switch the language and read the title of the translated article.
This tool automates that process.

## Usage

Let's translate the term "Linear algebra" from English to Russian:

```bash
>>> wikit "linear algebra" en ru
Линейная алгебра
```

## Installation

```bash
git clone git@github.com:asgervelling/wikitranslator.git
cd wikitranslator
pip install .
```


### Proxy servers

If you wanna use proxy servers, you can add them in .env:

```
http_proxy='http://proxy_1.com:port'
http_proxys='http://proxy_2.com:port'
```

Then you can choose to use proxy servers using the -p (--proxy) flag:

`wikit -p "Vand" dan german`