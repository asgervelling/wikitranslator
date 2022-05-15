import wikit.translations as translations
from wikit.languages import is_language, language_codes

import click


@click.command()
@click.option('--codes', is_flag=True)
@click.argument('term', )
@click.argument('from_lang')
@click.argument('to_lang')
def translate(term, from_lang, to_lang, codes=None):
    """ >>> "Water" en de -> "Wasser" """
    # Show language codes if requested
    if codes:
        print("hiii")

    try:
        args_are_valid(term, from_lang, to_lang)
    except click.BadParameter as e:
        click.echo(e)
        return

    

    translation = translations.translate(term, from_lang, to_lang)
    click.echo(translation)



def usage():
    click.echo("""
    Usage:
        >>> "linear algebra" en ru
        Линейная алгебра
    """)

def args_are_valid(term, from_lang, to_lang):
    if not is_language(from_lang):
        usage()
        raise click.BadParameter(f'{from_lang} is not a language')
    if not is_language(to_lang):
        usage()
        raise click.BadParameter(f'{to_lang} is not a language')
    return True

if __name__ == '__main__':
    translate()