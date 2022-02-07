import argparse
import os
import shutil
from os.path import exists, dirname, join, basename
from os import makedirs
from tempfile import mktemp, mkdtemp
from typing import List
import gettext
from platform import system, machine

import requests
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, InvalidArgumentException
from tqdm import tqdm
import tarfile
from waexceptions import WebArchiveException

_ = gettext.gettext
# Constants
PHANTOM = 'PHANTOM'
FIREFOX = 'FIREFOX'
CHROME = 'CHROME'
IS = 'IS'
ORG = 'ORG'
# Real drivers names
DRIVERS = {
    PHANTOM: {
        'driver_name': 'phantomjs',
        'download': {
            'windows': 'https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-windows.zip',
            'macos': 'https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-macosx.zip',
            'linux': {
                'x86_64': 'https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2',
                'i686': 'https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-i686.tar.bz2'
            }
        }
    },
    FIREFOX: {
        'driver_name': 'geckodriver',
        'download': {
            'windows': 'https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-win32.zip',
            'linux': {
                'x86_64': 'https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz',
                'i686': 'https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux32.tar.gz'
            }
        }
    },
    CHROME: 'chormedriver'
}


class ArgumentError(Exception):
    pass


def download_driver(driver_path: str, browser: str, os_name: str, arch: str):
    folder = dirname(driver_path)
    if not exists(folder):
        makedirs(folder)
    url = DRIVERS[browser]['download'][os_name][arch]
    r = requests.get(url, stream=True)
    if r.ok:
        tmp = mkdtemp()
        file_type, file_size = r.headers['content-type'], int(r.headers['Content-Length'])
        t = tqdm(total=file_size, desc='Downloading driver')
        tar_tmp = join(tmp, 'phantomjs.tar')
        with open(tar_tmp, 'wb') as file:
            for chunk in r:
                t.update(len(chunk))
                file.write(chunk)
        t.close()
        with tarfile.open(tar_tmp, "r") as tar:
            tar.extract('phantomjs-2.1.1-linux-x86_64/bin/phantomjs', tmp)
        shutil.move(join(tmp, 'phantomjs-2.1.1-linux-x86_64/bin/phantomjs'), driver_path)
        shutil.rmtree(tmp)
    else:
        raise ValueError(f'The url "{url}" does not contain any driver to download')



class ArgumentParser(object):
    """
    Argument parser for webarchive.
    """

    @property
    def urls(self) -> List[str]:
        return self._args.urls

    @property
    def browser(self) -> str:
        return self.get_suitable_driver(self._args.browser)

    @property
    def archive(self) -> str:
        return self._args.archive

    @property
    def delay(self) -> int:
        return self._args.delay

    @property
    def level(self) -> int:
        return self._args.level

    @property
    def secure(self) -> bool:
        return self._args.secure

    @property
    def force(self) -> bool:
        return self._args.force

    @property
    def subdomain(self) -> bool:
        return self._args.subdomain

    @property
    def verbose(self) -> bool:
        return self._args.verbose

    @property
    def hash(self) -> bool:
        return self._args.hash

    @property
    def only(self) -> bool:
        return self._args.only

    @property
    def update(self) -> bool:
        return self._args.update

    def __init__(self):
        parser = argparse.ArgumentParser(
            description=_('Rastrea una o varias webs y archiva cada una de las páginas en la web archive.is.'))
        parser.add_argument('urls', metavar='URL', type=str, nargs='+', help=_('lista de URLs o dominios a rastrear.'))
        parser.add_argument('-b', '--browser', metavar='BROWSER', type=str, default=PHANTOM,
                            choices=[PHANTOM, CHROME, FIREFOX],
                            help=_('El navegador utilizado en el rastreo. Por defecto es {0} que un navegador que no '
                                   'requiere interfaz y se ejecuta de forma oculta. '
                                   'Los valores disponibles son {0},{1},{2}'.format(PHANTOM, CHROME, FIREFOX)))
        parser.add_argument('-a', '--archive', metavar='ARCHIVE', type=str, default=IS,
                            choices=[IS, ORG],
                            help=_('La Web de archivo a utilizar, {0} para archive.is o {1} para archive.org. '
                                   'Por defecto se utilizará {0}. TODAVÍA NO ESTÁ IMPLEMENTADO'.format(IS, ORG)))
        parser.add_argument('-d', '--delay', metavar='VALUE', type=int, default=3,
                            help=_('Tiempo de espera entre peticiones a archive.is en segundos. Por defecto 3.'))
        parser.add_argument('-l', '--level', metavar='VALUE', type=int, default=-1,
                            help=_('El nivel máximo que debe alcanzar a partir de la página original, '
                                   '-1 si se quiere rastrear toda. Por defecto -1.'))
        parser.add_argument('-s', '--secure', default=False, action="store_true",
                            help=_('Rastreo en modo seguro, mucho más lento pero permite rastrear webs formadas '
                                   'enteramente con javascript y realiza también esperas en la web a rastrear.'
                                   'TODAVÍA NO ESTÁ IMPLEMENTADO.'))
        parser.add_argument('-f', '--force', default=False, action="store_true",
                            help=_('Vuelve a rastrear la web original y crear una nueva lista de enlaces. '
                                   'Tambien Fuerza un nuevo almacenamiento en archive.is aunque la web ya esté '
                                   'almacenada previamente. LA SEGUNDA PARTE TODAVÍA NO ESTÁ IMPLEMENTADA'))
        parser.add_argument('--subdomain', default=True, action="store_false",
                            help=_('Si se activa, no también en los subdominos que encuentre. '
                                   'Útil para páginas en WordPress o que no tienen su propio dominio.'))
        parser.add_argument('-v', '--verbose', default=False, action="store_true",
                            help=_('Muestra más información por pantalla.'))
        parser.add_argument('-H', '--hash', default=True, action="store_false",
                            help=_('Sigue siempre los enlaces que tengan # o ?, útil para páginas con AngularJS o CMS '
                                   'que no tienen activado las URLs limpias.'))
        parser.add_argument('-o', '--only', default=False, action="store_true",
                            help=_('Rastrea los enlaces de la página pero no los almacena en archive.'))
        parser.add_argument('-u', '--update', default=False, action="store_true",
                            help=_('Actualiza la lista de enlaces encontrados antes de archivar la web. '))

        self._args = parser.parse_args()

    def get_suitable_driver(self, browser):
        try:
            driver_file = DRIVERS[browser]['driver_name'] if isinstance(DRIVERS[browser], dict) else DRIVERS[browser]
            os_name: str = system().lower()
            arch: str = machine()
            driver_path = self.get_driver_path(driver_file, os_name, arch)
            if not exists(driver_path):
                download_driver(driver_path, browser, os_name, arch)
            if browser == PHANTOM:
                return webdriver.PhantomJS(driver_path)
            elif browser == FIREFOX:
                # options = Options()
                # options.headless = True
                # driver = webdriver.Firefox(options=options,
                #                            executable_path=r'C:\Utility\BrowserDrivers\geckodriver.exe')
                return webdriver.Firefox(firefox_binary='/usr/bin/firefox')
            elif browser == CHROME:
                return webdriver.Chrome(driver_path)
        except KeyError:
            raise ArgumentError("The navegador '{0}' no está contemplado en esta versión".format(browser))
        except WebDriverException as e:
            raise WebDriverException(f'The specific driver has to be in the path "{driver_path}": {str(e)}')

    @staticmethod
    def get_driver_path(fname: str, os_name: str, arch: str) -> str:
        if os_name == 'windows':
            return f'selenium/windows/{fname}.exe'
        if os_name == 'linux':
            return f'selenium/{os_name}/{arch}/{fname}'
        return f'selenium/{os_name}/{fname}'
        # raise WebArchiveException(f'The Operating System "{os_name}" is not supported yet.')
