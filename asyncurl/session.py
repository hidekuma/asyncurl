import requests

class AsyncURLSession(requests.Session):
    def __init__(self, fetch_method='GET', fetch_url=None):
        super().__init__()
        self.headers = {
            'User-Agent': 'AsyncURLBot/1.0.0 (+AsyncURLBot;)',
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'Connection': 'keep-alive'
        }
        self._fetch_method = fetch_method
        self._fetch_url = fetch_url
        self.__list_of_method = ('GET', 'POST', 'PUT', 'DELETE')

    @property
    def fetch_method(self):
        return self._fetch_method

    @fetch_method.setter
    def fetch_method(self, fetch_method):
        if isinstance(fetch_method, str):
            fetch_method = fetch_method.upper()
            if fetch_method in self.__list_of_method:
                self._fetch_method = fetch_method
            else:
                raise ValueError('Can accept methods are {1}.'.format(fetch_method, self.__list_of_method))
        else:
            raise ValueError('{0} is not String.'.format(fetch_method))

    @property
    def fetch_url(self):
        return self._fetch_url

    @fetch_url.setter
    def fetch_url(self, fetch_url):
        if isinstance(fetch_url, str):
            self._fetch_url = fetch_url
        else:
            raise ValueError('{0} is not String.'.format(fetch_url))

