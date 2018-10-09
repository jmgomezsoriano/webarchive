# Required modules: requests, selenium, tqdm, lxml, urllib3
import sys
import re
import json
from time import sleep
import os.path
import lxml.html
import hashlib
import argparse

from platform import system
from requests.exceptions import SSLError
from requests.exceptions import ConnectionError
from urllib3.exceptions import NewConnectionError
from tqdm import tqdm
from selenium import webdriver
from selenium.common.exceptions import InvalidArgumentException, InvalidElementStateException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from waexceptions import WebArchiveException
import traceback
import requests
import re
from urllib.parse import urlsplit
from pathlib import Path


# Constantes
PHANTOM = "PHANTOM"
FIREFOX = "FIREFOX"
CHROME = "CHROME"
IS = "IS"
ORG = "ORG"
LINKS_FILE_NAME = "links.txt"
LOG_FILE_NAME = "archived.log"
MAXIMUM_ATTEMPTS = 5 # Number of intents
LONG_PERIOD_WAIT = 60 * 5 # Wait 5 minutes

# Listas globales
visited = set()
pages = set()
sha1pages = set()
archived = set()

# Default arguments
verbose: bool = False
delay: int = 3
archive = 'is'
level =0

# Calculate the app configuration directory
home = str(Path.joinpath(Path.home(), '.webarchive'))


def parser_arguments() -> argparse.ArgumentParser:
    """

    :rtype: object
    """
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

    return parser.parse_args()


def wait(driver, delay = 3):
    WebDriverWait(driver, delay)


def wait_for_xpath(driver, xpath, timeout = 5):
    try:
        elem = EC.presence_of_element_located((By.XPATH, xpath))
        WebDriverWait(driver, timeout).until(elem)
    except TimeoutException:
        return False
    return True


def check_exists_by_xpath(xpath):
    try:
        webdriver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


def verbMsg(msg):
    if verbose:
        print(msg)


def store_link(domain, url: str):
    file = open(get_file_path(domain, LOG_FILE_NAME), "a")
    file.write(url + '\n')
    file.close()


def archive_is_page(driver, domain, url):
    try:
        verbMsg("Cargando la página principal...")
        driver.get("http://archive.is")
        verbMsg("Página principal cargada, buscando la barra de búsqueda...")
        elem = driver.find_element_by_name("url")
        verbMsg("Esperando {0} segundos.".format(delay))
        wait_for_xpath(driver, "/inexistente_path", delay)
        # sleep(delay)
        # WebDriverWait(driver, delay)
        # driver.implicitly_wait(delay)
        verbMsg("Escribiendo la dirección.")
        elem.send_keys(url)
        verbMsg("Buscando el botón.")
        elem = driver.find_element_by_xpath("//input[@value = 'archivar']")
        verbMsg("Pulsando el botón...")
        elem.click()
        verbMsg("Esperando a la página de loading para {0}".format(url))
        count = 0
        while not wait_for_xpath(driver, "//input[@value = 'guardar la página']", 1) \
                and not wait_for_xpath(driver, "/html/body/div[span = 'Loading.']", 1) \
                and not wait_for_xpath(driver, "//td[a = 'Página']", 1) and count < MAXIMUM_ATTEMPTS:
            count += 1
            verbMsg("Waitted {0} of {1} seconds.".format(count * 3, MAXIMUM_ATTEMPTS * 3))
        if count == MAXIMUM_ATTEMPTS:
            verbMsg("Timeout to add: {0}\n".format(url))
        else:
            wait_for_xpath(driver, "/inexistente_path", delay)
            #driver.implicitly_wait(delay)
            if wait_for_xpath(driver, "//input[@value = 'guardar la página']", 1):
                verbMsg("Page already add: {0}".format(url))
                store_link(domain, url)
            else:
                verbMsg("Esperando a la página almacenada")
                if wait_for_xpath(driver, "//td[a = 'Página']", 60):
                    verbMsg("Page succesfuly add {0}".format(url))
                    store_link(domain, url)
                else:
                    verbMsg("Timeout to add: {0}\n".format(url))
            wait_for_xpath(driver, "/inexistente_path", delay)
    except NoSuchElementException:
        verbMsg("La página principal de archive.is no se carga, esperando {0} segundos.".format(LONG_PERIOD_WAIT))
        wait_for_xpath(driver, "/inexistente_path", LONG_PERIOD_WAIT)
    except InvalidElementStateException:
        verbMsg("La página principal de archive.is no se carga, esperando {0} segundos.".format(LONG_PERIOD_WAIT))
        wait_for_xpath(driver, "/inexistente_path", LONG_PERIOD_WAIT)


def search_urls(driver, url):
    driver.get(url)
    return [x.get_attribute("href") for x in driver.find_elements_by_xpath("//a[@href]")]


def build_url(base, path):
    if re.match("^[a-zA-Z]+:.*", path) is not None:
        return path
    elif path.startswith("/"):
        return base + path[1:len(path)]
    return base + path


def get_domain(url):
    return "{0.scheme}://{0.netloc}/".format(urlsplit(url))


def search_urls_wget(url: str, subdomain: bool):
    response = requests.get(url)
    if not response.status_code == 200:
        return []
    sha1 = hashlib.sha1(response.text.encode()).hexdigest()
    if sha1 in sha1pages:
        pages.remove(url)
        return []
    sha1pages.add(sha1)
    try:
        page = lxml.html.fromstring(response.text)
        base = get_domain(response.url, subdomain)
        return [build_url(base, x.get('href')) for x in page.xpath('//a') if x.get('href') is not None]
    except ValueError:
        return []


def crawl_web(domain: str, driver, url, level: int, subdomain: bool):
    # Normalize the url
    if hash:
        pos = url.find('#')
        if pos != -1:
            url = url[:pos]
        pos = url.find('?')
        if pos != -1:
            url = url[:pos]
    if url.endswith('#'):
        url = url[0:-1]
    if url.endswith('/'):
        url = url[0:-1]
    # Check if the url has already been visited or it is an email link or it is from other domain
    if url in visited or url.startswith("mailto:") or \
            not re.match(r"^[^:]+://((\w|-|_)+\.)*{0}(/.*|$)".format(domain), url):
        return False
    try:
        # Get the link content type and crawl only the text ones
        response = requests.head(url)
        # Add the url to the visited ones
        visited.add(url)
        content_type = response.headers.get("Content-type").split(";")[0]
        verbMsg("{0}: {1}".format(url, content_type))
        if content_type in ["text/html", "application/pdf", "application/rss+xml"]:
            pages.add(url)
            print("\rEncontradas {0} páginas.".format(len(pages)), end='\n' if verbose else ' ')
            if content_type in ["text/html"]:
                for u in search_urls_wget(url, subdomain):
                    if level != 0:
                        try:
                            crawl_web(domain, driver, u, level - 1, subdomain)
                        except RecursionError:
                            print("Límite de recursión alcanzado con la url '{0}'.".format(u))
        elif content_type not in ["image/jpeg", "image/png"]:
            print("Content type '{0}' have not recognized.".format(content_type), file=sys.stderr)
        else:
            verbMsg("Ignoring '{0}' content type.".format(content_type))
    except SSLError as ex:
        print("The URL '{0}' has not be able to crawl caused by a SSL Error: {1}".format(url, str(ex)), file=sys.stderr)
    except ConnectionError as ex:
        print("The URL '{0}' has not be able to crawl caused by a Connection Error: {1}".format(url, str(ex)), file=sys.stderr)
    except NewConnectionError as ex:
        print("The URL '{0}' has not be able to crawl caused by a New Connection Error {1}.".format(url, str(ex)), file=sys.stderr)


def get_file_path(domain: str, file: str):
    dir = get_domain_dir(domain)
    return Path.joinpath(dir, file)


def exists_file(domain: str, file: str):
    return Path.exists(get_file_path(domain, file))


def get_domain_dir(domain: str):
    domain_dir = Path.joinpath(Path(home), domain)
    Path.mkdir(domain_dir, parents=True, exist_ok=True)

    return domain_dir


def store_links(domain: str, pages: set):
    file = open(get_file_path(domain, LINKS_FILE_NAME), "w")
    for link in pages:
        file.write(link + "\n")
    file.close()


def load_file(domain: str, file: str):
    lines = set()
    path = get_file_path(domain, file)
    if Path.exists(path):
        links_file = open(path, "r")
        for link in links_file:
            lines.add(link[:-1])
        links_file.close()
    return lines


def get_suitable_driver(browser):
    if browser == PHANTOM:
        return webdriver.PhantomJS(get_driver_path('phantomjs'))
    elif browser == FIREFOX:
        return webdriver.Firefox(get_driver_path('geckodriver'))
    elif browser == CHROME:
        return webdriver.Chrome(get_driver_path('chormedriver'))
    else:
        raise InvalidArgumentException("The navegador '{0}' no está contemplado en esta versión".format(browser))


def get_driver_path(filename: str):
    os_name: str = system()
    if os_name == 'Windows':
        return 'selenium/windows/' + filename + '.exe'
    if os_name == 'Linux':
        return 'selenium/linux/' + filename

    raise WebArchiveException("The Operating System '{0}' does not supported.".format(os_name))




def delete_log_file(domain):
    if exists_file(domain, LOG_FILE_NAME):
        path = get_file_path(domain, LOG_FILE_NAME)
        os.remove(path)


def showStatistics(domain: str):
    archived = load_file(domain, LOG_FILE_NAME)
    pages = load_file(domain, LINKS_FILE_NAME)
    print('En el dominio {0} se ha encontrado {1} enlaces ' 
          'de los cuales se han archivado {2}.'.format(domain, len(pages), len(archived)))


def get_domain(url: str, subdomain: bool) -> str:
    if subdomain:
        return re.sub(r"^[^:]+://((\w|-|_)+\.)*((\w|-|_)+\.\w+)(/.*|$)", r"\g<3>", url)
    else:
        return re.sub(r"^[^:]+://(((\w|-|_)+\.)*((\w|-|_)+\.\w+))(/.*|$)", r"\g<1>", url)


def reuse_links(domain, force, update) -> str:
    return exists_file(domain, LINKS_FILE_NAME) and not force and not update


def load_links(domain):
    archived = load_file(domain, LOG_FILE_NAME)
    pages = load_file(domain, LINKS_FILE_NAME)
    pages -= archived
    return pages

def main():
    # Parse command line arguments
    args = parser_arguments()
    driver = get_suitable_driver(args.browser)
    global verbose, delay, archived, level, pages, hash
    verbose = args.verbose
    delay = args.delay
    level = args.level
    hash = args.hash

    try:
        # For each url to crawl
        for url in args.urls:
            # Obtain the domain and crawl
            domain = get_domain(url, args.subdomain)


            # si el dominio ya ha sido rastreado, carga la lista de links obtenidas
            if reuse_links(domain, args.force, args.update):
                print("El dominio '{0}' ya ha sido rastreado. Se usará la lista previa de enlaces. "
                      "Use -f para evitarlo o -u para actualizarla.".format(domain))
                pages = load_links(domain)
            else:
                # En caso contrario rastrea y almacena los links encontrados
                print("Rastreando el dominio '{0}'. Esto puede tardar un rato.".format(domain))
                crawl_web(domain, driver, url, level, args.subdomain)
                store_links(domain, pages)
                if args.force:
                    delete_log_file(domain)
            if not verbose:
                print()

            if not args.only:
                # Archivo las páginas encontradas
                tqdm.ncols = 120
                for link in tqdm(pages, dynamic_ncols=True):
                    if args.archive == IS:
                        archive_is_page(driver, domain, link)
                    else:
                        raise InvalidArgumentException('En estos momentos solo está permitida la web de archive.is.')

            showStatistics(domain)
    except InvalidArgumentException as ex:
        if args.verbose:
            traceback.print_exc()
        else:
            sys.stderr.write('ERROR DE ARGUMENTOS: {0}\n'.format(ex.msg))
    driver.close()


if __name__ == "__main__":
    main()