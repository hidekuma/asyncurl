from requests import Request, Session

class AsyncURLSession(Session):
    def __init__(self, method, url, *, params=None, data=None, headers=None, cookies=None, files=None,
            auth=None, timeout=None, allow_redirects=True, proxies=None,
            hooks=None, stream=None, verify=None, cert=None, json=None):

        """Constructs a :class:`Request <Request>`, prepares it.
        :param method: method for the new :class:`Request` object.
        :param url: URL for the new :class:`Request` object.
        :param params: (optional) Dictionary or bytes to be sent in the query
            string for the :class:`Request`.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) json to send in the body of the
            :class:`Request`.
        :param headers: (optional) Dictionary of HTTP Headers to send with the
            :class:`Request`.
        :param cookies: (optional) Dict or CookieJar object to send with the
            :class:`Request`.
        :param files: (optional) Dictionary of ``'filename': file-like-objects``
            for multipart encoding upload.
        :param auth: (optional) Auth tuple or callable to enable
            Basic/Digest/Custom HTTP Auth.
        :param timeout: (optional) How long to wait for the server to send
            data before giving up, as a float, or a :ref:`(connect timeout,
            read timeout) <timeouts>` tuple.
        :type timeout: float or tuple
        :param allow_redirects: (optional) Set to True by default.
        :type allow_redirects: bool
        :param proxies: (optional) Dictionary mapping protocol or protocol and
            hostname to the URL of the proxy.
        :param stream: (optional) whether to immediately download the response
            content. Defaults to ``False``.
        :param verify: (optional) Either a boolean, in which case it controls whether we verify
            the server's TLS certificate, or a string, in which case it must be a path
            to a CA bundle to use. Defaults to ``True``.
        :param cert: (optional) if String, path to ssl client cert file (.pem).
            If Tuple, ('cert', 'key') pair.
        :rtype: requests.Response
        """

        super().__init__()
        #self.__list_of_method = ('GET', 'POST', 'PUT', 'DELETE')

        if headers is None:
            headers = {
                'User-Agent': 'AsyncURLBot/1.0.0 (+AsyncURLBot;)',
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'Connection': 'keep-alive'
            }

        req = Request(
            method=method.upper(),
            url=url,
            headers=headers,
            files=files,
            data=data or {},
            json=json,
            params=params or {},
            auth=auth,
            cookies=cookies,
            hooks=hooks,
        )
        self._fetch_prep = self.prepare_request(req)

        proxies = proxies or {}

        settings = self.merge_environment_settings(
            self._fetch_prep.url, proxies, stream, verify, cert
        )

        self._fetch_send_kwargs = {
            'timeout': timeout,
            'allow_redirects': allow_redirects,
        }

        self._fetch_send_kwargs.update(settings)

    def send(self):
        """
        Send prepared request.
        Returns :class:`Response <Response>` object.
        """
        #print(self._fetch_prep.__dict__)
        #print(self._fetch_send_kwargs)
        return super().send(self._fetch_prep, **self._fetch_send_kwargs)
