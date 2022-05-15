
import click

""" import wikit.translations as translations
from wikit.languages import get_language_code, is_language """
from .translations import translate
from .languages import get_language_code, is_language


@click.command()
@click.option('-p', '--proxy', is_flag=True,
              help='Use proxies set in .env')
@click.argument('term', )
@click.argument('from_lang')
@click.argument('to_lang')
def main(term, from_lang, to_lang, proxy=False):
    """ >>> "Water" en de -> "Wasser" """
    try:
        args_are_valid(term, from_lang, to_lang)
    except click.BadParameter as e:
        click.echo(e)
        return

    from_ = get_language_code(from_lang)
    to_ = get_language_code(to_lang)

    translation = translate(
        term,
        from_,
        to_,
        use_proxies=proxy
    )
    click.echo(translation)


def usage():
    click.echo("""
    Usage:
        >>> "linear algebra" en ru
        Линейная алгебра

        >>> "Substitutionsmetoden" danish Malay
        Persamaan serentak
    """)


def args_are_valid(term, from_lang, to_lang):
    if not is_language(from_lang):
        usage()
        raise click.BadParameter(f'{from_lang} is not a language')
    if not is_language(to_lang):
        usage()
        raise click.BadParameter(f'{to_lang} is not a language')
    return True


def language_valid(lang):
    return is_language(lang)


if __name__ == '__main__':
    main()
