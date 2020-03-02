from abc import ABC, ABCMeta, abstractmethod
from time import time


class AbstractBrowser(object):
    __metaclass__ = ABCMeta
    last_time = 0

    def go(self, url: str):
        self._wait()
        try:
            return self._go(url)
        finally:
            self._last_time = time()

    @abstractmethod
    def _go(self, url):
        pass

    @abstractmethod
    def _wait(self, elapsed):
        pass

    @abstractmethod
    def head(self):
        pass


class Requests(AbstractBrowser, ABC):
    def __init__(self, delay: int):
        self._delay = delay

    def _go(self):
        pass

    def _wait(self):
        pass

    def head(self):
        pass

