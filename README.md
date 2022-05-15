![Tests](https://github.com/asgervelling/wikitranslator/actions/workflows/tests.yml/badge.svg)

# Wikitranslator

## Translate using Wikipedia

Typically when I can't find a translation in a dictionary, I find its article on Wikipedia in the language I want to translate from, switch the language and read the title of the translated article.
This tool automates that process.

## Installation

```bash
git clone git@github.com:asgervelling/wikitranslator.git
cd wikitranslator
pip install .
```

## Usage

Let's translate the term "Linear algebra" from English to Russian:

```bash
>>> wikit "linear algebra" en ru`
Линейная алгебра
```
