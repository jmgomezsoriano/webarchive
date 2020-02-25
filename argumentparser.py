import argparse
from os.path import isdir
from typing import AnyStr


class ArgumentError(Exception):
    pass


class ArgumentParser(object):
    """
    Argument parser for the searcher.
    """

    @property
    def index_dir(self) -> AnyStr:
        """ The index folder to store the index files. """
        return self._index_dir

    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Rastrea una o varias webs y archiva cada una de las páginas en la web archive.is.')
        parser.add_argument('urls', metavar='URL', type=str, nargs='+', help='lista de URLs o dominios a rastrear.')
        parser.add_argument('-b', '--browser', metavar='BROWSER', type=str, default=PHANTOM,
                            choices=[PHANTOM, CHROME, FIREFOX],
                            help='El navegador utilizado en el rastreo. Por defecto es {0} que un navegador que no '
                                 'requiere interfaz y se ejecuta de forma oculta. '
                                 'Los valores disponibles son {0},{1},{2}'.format(PHANTOM, CHROME, FIREFOX))
        parser.add_argument('-a', '--archive', metavar='ARCHIVE', type=str, default=IS,
                            choices=[IS, ORG],
                            help='La Web de archivo a utilizar, {0} para archive.is o {1} para archive.org. '
                                 'Por defecto se utilizará {0}. TODAVÍA NO ESTÁ IMPLEMENTADO'.format(IS, ORG))
        parser.add_argument('-d', '--delay', metavar='VALUE', type=int, default=3,
                            help='Tiempo de espera entre peticiones a archive.is en segundos. Por defecto 3.')
        parser.add_argument('-l', '--level', metavar='VALUE', type=int, default=-1,
                            help='El nivel máximo que debe alcanzar a partir de la página original, '
                                 '-1 si se quiere rastrear toda. Por defecto -1.')
        parser.add_argument('-s', '--secure', default=False, action="store_true",
                            help='Rastreo en modo seguro, mucho más lento pero permite rastrear webs formadas enteramente '
                                 'con javascript y realiza también esperas en la web a rastrear. TODAVÍA NO ESTÁ '
                                 'IMPLEMENTADO.')
        parser.add_argument('-f', '--force', default=False, action="store_true",
                            help='Vuelve a rastrear la web original y crear una nueva lista de enlaces. Tambien Fuerza un '
                                 'nuevo almacenamiento en archive.is aunque la web ya esté almacenada previamente.'
                                 'LA SEGUNDA PARTE TODAVÍA NO ESTÁ IMPLEMENTADA')
        parser.add_argument('--subdomain', default=True, action="store_false",
                            help='Si se activa, no también en los subdominos que encuentre. '
                                 'Útil para páginas en WordPress o que no tienen su propio dominio.')
        parser.add_argument('-v', '--verbose', default=False, action="store_true",
                            help='Muestra más información por pantalla.')
        parser.add_argument('-H', '--hash', default=True, action="store_false",
                            help='Sigue siempre los enlaces que tengan # o ?, útil para páginas con AngularJS o CMS que no '
                                 'tienen activado las URLs limpias.')
        parser.add_argument('-o', '--only', default=False, action="store_true",
                            help='Rastrea los enlaces de la página pero no los almacena en archive.')
        parser.add_argument('-u', '--update', default=False, action="store_true",
                            help='Actualiza la lista de enlaces encontrados antes de archivar la web. '
                                 'TODAVÍA NO ESTÁ IMPLEMENTADO')

