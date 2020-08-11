# Required modules: requests, selenium, tqdm, lxml, urllib3
import sys
import re
import json
from time import sleep
import os.path
import lxml.html
import hashlib
import argparse
import gettext
from platform import system

from requests import Response
from requests.exceptions import SSLError, ReadTimeout
from requests.exceptions import ConnectionError
from urllib3.exceptions import NewConnectionError
from tqdm import tqdm
from selenium.common.exceptions import InvalidArgumentException, InvalidElementStateException, WebDriverException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from argumentparser import ArgumentParser, IS
from waexceptions import WebArchiveException
import traceback
import requests
import re
from urllib.parse import urlsplit
from pathlib import Path

# Internationalization
_ = gettext.gettext
# Constants
LINKS_FILE_NAME = "links.txt"
LOG_FILE_NAME = "archived.log"
MAXIMUM_ATTEMPTS = 20 # Number of intents
LONG_PERIOD_WAIT = 60 * 5 # Wait 5 minutes
TIMEOUT = 3

# Global lists
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
        elem = driver.find_element_by_xpath("//input[@value = 'save']")
        verbMsg("Pulsando el botón...")
        elem.click()
        verbMsg("Esperando a la página de loading para {0}".format(url))
        count = 0
        while not wait_for_xpath(driver, "//input[@value = 'guardar la página']", 3) \
                and not wait_for_xpath(driver, "/html/body/div[span = 'Loading.']", 3) \
                and not wait_for_xpath(driver, "//td[a = 'Página']", 3) and count < MAXIMUM_ATTEMPTS:
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
                if wait_for_xpath(driver, '//div[@id="HEADER"]', 120):
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


def get_domain(url: str):
    return "{0.scheme}://{0.netloc}/".format(urlsplit(url))


def search_urls_wget(url: str, subdomain: bool):

    response = timeout(url, TIMEOUT)

    if not response or not response.status_code == 200:
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


def timeout(url: str, timeout: float = TIMEOUT, func=requests.get, intents: int = 3) -> Response:
    for i in range(intents):
        try:
            return func(url, timeout=timeout * (i * 30 + 1))
        except ReadTimeout:
            print(f'Timeout {url}: trying again. Left {intents - i - 1} intents.', file=sys.stderr)
    return None


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
        response = timeout(url, TIMEOUT, requests.head)
        # response = requests.head(url, timeout=TIMEOUT)
        if response and response.ok:
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
    args = ArgumentParser()
    global verbose, delay, archived, level, pages, hash
    verbose = args.verbose
    delay = args.delay
    level = args.level
    hash = args.hash
    try:
        driver = args.browser

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
    except WebDriverException as e:
        print(str(e), file=sys.stderr)


if __name__ == "__main__":
    main()
