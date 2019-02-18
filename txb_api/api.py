# -*- coding: utf-8 -*-

import requests

from time import sleep


class API:
    API_URL = 'https://api.exchange.3xbit.com.br'

    CLIENT_API_VERSION = 'v1'
    PUBLIC_API_VERSION = 'v1'

    TIMEOUT_IN_SECONDS = 15

    DEPOSIT_CANCELED = 'CANCELED'
    DEPOSIT_PENDING = 'PENDING'
    DEPOSIT_DONE = 'DONE'

    WITHDRAW_CANCELED = 'CANCELED'
    WITHDRAW_PENDING = 'PENDING'
    WITHDRAW_DONE = 'DONE'

    ORDER_BUY = 'BUY'
    ORDER_SELL = 'SELL'
    ORDER_LIMIT = 'LIMIT'
    ORDER_MARKET = 'MARKET'
    ORDER_PENDING = 'PENDING'
    ORDER_DONE = 'DONE'
    ORDER_LAST_24H = '24H'

    @property
    def _headers(self) -> dict:
        """
        :return: Headers
        """
        default_headers = requests.utils.default_headers()
        user_agent = 'python-txb-api/' + default_headers.get('User-Agent', '')
        headers = {
            'User-Agent': user_agent,
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        return headers

    def _request(self, method: str, url: str, **kwargs) -> any:
        """
        :param method: method for the new :class:`Request` object.
        :param url: URL for the new :class:`Request` object.
        :param params: (optional) Dictionary or bytes to be sent in the query string for the :class:`Request`.
        :param data: (optional) Dictionary or list of tuples ``[(key, value)]`` (will be form-encoded), bytes,
            or file-like object to send in the body of the :class:`Request`.
        :param json: (optional) json data to send in the body of the :class:`Request`.
        :param headers: (optional) Dictionary of HTTP Headers to send with the :class:`Request`.
        :param cookies: (optional) Dict or CookieJar object to send with the :class:`Request`.
        :param files: (optional) Dictionary of
            ``'name': file-like-objects`` (or ``{'name': file-tuple}``) for multipart encoding upload.
            ``file-tuple`` can be a 2-tuple ``('filename', fileobj)``, 3-tuple ``('filename', fileobj, 'content_type')``
            or a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``, where ``'content-type'`` is a string
            defining the content type of the given file and ``custom_headers`` a dict-like object containing
            additional headers to add for the file.
        :param auth: (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
        :param timeout: (optional) How many seconds to wait for the server to send data
            before giving up, as a float, or a :ref:`(connect timeout, read timeout) <timeouts>` tuple.
        :type timeout: float or tuple
        :param allow_redirects: (optional) Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection.
            Defaults to ``True``.
        :type allow_redirects: bool
        :param proxies: (optional) Dictionary mapping protocol to the URL of the proxy.
        :param verify: (optional) Either a boolean, in which case it controls whether we verify
            the server's TLS certificate, or a string, in which case it must be a path
            to a CA bundle to use. Defaults to ``True``.
        :param stream: (optional) if ``False``, the response content will be immediately downloaded.
        :param cert: (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.

        :return: bool if method == 'DELETE' else list or dict
        :rtype: any
        """
        kwargs['headers'] = kwargs.get('headers') or self._headers
        payload = requests.request(method, url, timeout=self.TIMEOUT_IN_SECONDS, **kwargs)
        try:
            payload.raise_for_status()
        except requests.HTTPError as e:
            if e.response.status_code == 429:
                sleep(1)
                return self._request(method, url, **kwargs)
            print(e.response.content)
            raise
        response = payload.ok if method == 'DELETE' else payload.json()
        return response
