from urllib.request import urlopen
import time


class WebPage:
    TIME_LIMIT = 900

    def __init__(self, url):
        self.url = url
        self._content = None
        self._last_updated = 0

    @property
    def content(self):
        if not self._content or abs(time.time() - self._last_updated) > WebPage.TIME_LIMIT:
            print("Retrieving New Page...")
            self._content = urlopen(self.url).read()
            self._last_updated = time.time()
        return self._content
