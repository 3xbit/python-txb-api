# -*- coding: utf-8 -*-

from txb_api.api import API


class Public(API):

    def ticker(self, convert_to: str=None) -> dict:
        url = '{api_url}/ticker/'.format(api_url=self.API_URL)
        if convert_to:
            url += convert_to
        ticker = self._request('GET', url)
        return ticker

    def orderbook(self, currency_price: str, currency_quantity: str, currency_rate: str=None) -> dict:
        url = '{api_url}/{api_version}/orderbook/{currency_price}/{currency_quantity}/'.format(
            api_url=self.API_URL,
            api_version=self.PUBLIC_API_VERSION,
            currency_price=currency_price,
            currency_quantity=currency_quantity,
        )
        params = {'currency_rate': currency_rate} if currency_rate else {}
        orderbook = self._request('GET', url, params=params)
        return orderbook

    def market_history(self, currency_price: str, currency_quantity: str, currency_rate: str=None,
                       page: int=1, since: float=None, until: float=None) -> dict:
        url = '{api_url}/{api_version}/history/{currency_price}/{currency_quantity}/'.format(
            api_url=self.API_URL,
            api_version=self.PUBLIC_API_VERSION,
            currency_price=currency_price,
            currency_quantity=currency_quantity,
        )

        params = {}
        if currency_rate:
            params['currency_rate'] = currency_rate
        if page:
            params['page'] = page
        if since:
            params['since'] = since
        if until:
            params['until'] = until

        market_history = self._request('GET', url, params=params)
        return market_history
