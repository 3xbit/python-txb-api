# -*- coding: utf-8 -*-

import requests

from time import sleep


class API:

    API_URL = 'https://api.exchange.3xbit.com.br'

    CLIENT_API_VERSION = 'v1'
    PUBLIC_API_VERSION = 'v1'

    TIMEOUT_IN_SECONDS = 15

    ORDER_BUY = 'BUY'
    ORDER_SELL = 'SELL'
    ORDER_LIMIT = 'LIMIT'
    ORDER_MARKET = 'MARKET'

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
