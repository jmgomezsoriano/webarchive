# WebArchive
A tool to archive a complete web in archive.is or archive.org written in Python 3.

# Before to execute
It is necessary to install the following Python modules: requests, selenium, tqdm, lxml, urllib3

You can install these modules using pip:

pip install requests selenium tqdm lxml urllib3

# Execute

Without arguments you can see the minium command help:

usage: webarchive.py [-h] [-b BROWSER] [-a ARCHIVE] [-d VALUE] [-l VALUE] [-s]
                     [-f] [--subdomain] [-v] [-H] [-o] [-u]
                     URL [URL ...]
webarchive.py: error: the following arguments are required: URL

With the argument -h you can see more information:

usage: webarchive.py [-h] [-b BROWSER] [-a ARCHIVE] [-d VALUE] [-l VALUE] [-s]
                     [-f] [--subdomain] [-v] [-H] [-o] [-u]
                     URL [URL ...]

Rastrea una o varias webs y archiva cada una de las páginas en la web
archive.is.

positional arguments:
  URL                   lista de URLs o dominios a rastrear.

optional arguments:
  -h, --help            show this help message and exit
  -b BROWSER, --browser BROWSER
                        El navegador utilizado en el rastreo. Por defecto es
                        PHANTOM que un navegador que no requiere interfaz y se
                        ejecuta de forma oculta. Los valores disponibles son
                        PHANTOM,CHROME,FIREFOX
  -a ARCHIVE, --archive ARCHIVE
                        La Web de archivo a utilizar, IS para archive.is o ORG
                        para archive.org. Por defecto se utilizará IS. TODAVÍA
                        NO ESTÁ IMPLEMENTADO
  -d VALUE, --delay VALUE
                        Tiempo de espera entre peticiones a archive.is en
                        segundos. Por defecto 3.
  -l VALUE, --level VALUE
                        El nivel máximo que debe alcanzar a partir de la
                        página original, -1 si se quiere rastrear toda. Por
                        defecto -1.
  -s, --secure          Rastreo en modo seguro, mucho más lento pero permite
                        rastrear webs formadas enteramente con javascript y
                        realiza también esperas en la web a rastrear. TODAVÍA
                        NO ESTÁ IMPLEMENTADO.
  -f, --force           Vuelve a rastrear la web original y crear una nueva
                        lista de enlaces. Tambien Fuerza un nuevo
                        almacenamiento en archive.is aunque la web ya esté
                        almacenada previamente.LA SEGUNDA PARTE TODAVÍA NO
                        ESTÁ IMPLEMENTADA
  --subdomain           Si se activa, no también en los subdominos que
                        encuentre. Útil para páginas en WordPress o que no
                        tienen su propio dominio.
  -v, --verbose         Muestra más información por pantalla.
  -H, --hash            Sigue siempre los enlaces que tengan # o ?, útil para
                        páginas con AngularJS o CMS que no tienen activado las
                        URLs limpias.
  -o, --only            Rastrea los enlaces de la página pero no los almacena
                        en archive.
  -u, --update          Actualiza la lista de enlaces encontrados antes de
                        archivar la web. TODAVÍA NO ESTÁ IMPLEMENTADO
