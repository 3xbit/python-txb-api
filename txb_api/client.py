# -*- coding: utf-8 -*-

import requests

from decimal import Decimal

from txb_api.public import API
from txb_api.helpers import calc_order


class Client(API):

    def __init__(self, client_id: str, client_secret: str) -> None:
        self._client_id = client_id
        self._client_secret = client_secret
        self._access_token = self._get_access_token()

    @property
    def _headers(self) -> dict:
        """
        :return: Headers formatted with access_token
        """
        headers = super(Client, self)._headers
        headers['Authorization'] = 'Bearer {access_token}'.format(access_token=self._access_token)
        return headers

    def _request(self, method: str, url: str, **kwargs) -> any:
        try:
            return super(Client, self)._request(method, url, **kwargs)
        except requests.HTTPError as e:
            if e.response.status_code == 401:
                self._access_token = self._get_access_token()
                return self._request(method, url, **kwargs)
            raise

    def _get_access_token(self) -> str:
        """
        :return: Access Token
        """
        url = '{api_url}/api/oauth/token/'.format(api_url=self.API_URL)
        data = {
            'grant_type': 'client_credentials',
            'client_id': self._client_id,
            'client_secret': self._client_secret,
        }
        payload = requests.request('POST', url, data=data, timeout=self.TIMEOUT_IN_SECONDS)
        try:
            payload.raise_for_status()
        except requests.HTTPError:
            raise

        token = payload.json()
        return token.get('access_token')

    def balance(self, currency: str = None) -> any:
        url = '{api_url}/{api_version}/balance/'.format(api_url=self.API_URL, api_version=self.CLIENT_API_VERSION)
        if currency:
            url += currency
        balance = self._request('GET', url)
        return balance

    def list_deposits(self, currency: str, status: str = None) -> list:
        url = '{api_url}/{api_version}/deposit/{currency}/'.format(
            api_url=self.API_URL,
            api_version=self.CLIENT_API_VERSION,
            currency=currency,
        )
        params = {'status': status} if status else {}
        deposits = self._request('GET', url, params=params)
        return deposits

    def get_deposit(self, currency: str, tx_hash: str) -> dict:
        url = '{api_url}/{api_version}/deposit/{currency}/{hash}'.format(
            api_url=self.API_URL,
            api_version=self.CLIENT_API_VERSION,
            currency=currency,
            hash=tx_hash,
        )
        deposit = self._request('GET', url)
        return deposit

    def list_withdraws(self, currency: str, status: str = None) -> list:
        url = '{api_url}/{api_version}/withdraw/{currency}/'.format(
            api_url=self.API_URL,
            api_version=self.CLIENT_API_VERSION,
            currency=currency,
        )
        params = {'status': status} if status else {}
        withdraws = self._request('GET', url, params=params)
        return withdraws

    def get_withdraw(self, currency: str, tx_hash: str):
        url = '{api_url}/{api_version}/withdraw/{currency}/{hash}'.format(
            api_url=self.API_URL,
            api_version=self.CLIENT_API_VERSION,
            currency=currency,
            hash=tx_hash,
        )
        withdraw = self._request('GET', url)
        return withdraw

    def create_order(self, order_type: str,
                     currency_price: str, unit_price: Decimal, currency_quantity: str, quantity: Decimal = None,
                     total: Decimal = None, percent_balance: int = None,
                     execution_type: str = API.ORDER_LIMIT) -> dict:
        """
        You can enter Quantity or Total.

        :param order_type: BUY or SELL
        :param currency_price: Currency of Unit Price
        :param unit_price: Unit Price
        :param currency_quantity: Currency of Quantity
        :param quantity: (optional) Quantity
        :param total: (optional) Total
        :param percent_balance: (optional) Percentage of Currency Balance of Unit Price
        :param execution_type: LIMIT or MARKET
        """

        url = '{api_url}/{api_version}/order/{currency_price}/{currency_quantity}/{order_type}/'.format(
            api_url=self.API_URL,
            api_version=self.CLIENT_API_VERSION,
            currency_price=currency_price,
            currency_quantity=currency_quantity,
            order_type=order_type.lower(),
        )

        if percent_balance:
            available_balance = self.balance(currency_price).get('available_balance')
            total = Decimal(str(available_balance)) * percent_balance / 100

        market = currency_price + currency_quantity
        unit_price, quantity, total = calc_order(market, unit_price, quantity, total)

        data = {
            'execution_type': execution_type,
            'unit_price': unit_price,
            'quantity': quantity,
        }
        order = self._request('POST', url, data=data)
        return order

    def list_orders(self, order_type: str, currency_price: str, currency_quantity: str, filter_by: str = None) -> list:
        url = '{api_url}/{api_version}/order/{currency_price}/{currency_quantity}/{order_type}/'.format(
            api_url=self.API_URL,
            api_version=self.CLIENT_API_VERSION,
            currency_price=currency_price,
            currency_quantity=currency_quantity,
            order_type=order_type.lower(),
        )
        params = {'filter': filter_by} if filter_by else {}
        orders = self._request('GET', url, params=params)
        return orders

    def get_order(self, order_id: str) -> dict:
        url = '{api_url}/{api_version}/order/{order_id}/'.format(
            api_url=self.API_URL,
            api_version=self.CLIENT_API_VERSION,
            order_id=order_id,
        )
        order = self._request('GET', url)
        return order

    def cancel_order(self, order_id: str) -> bool:
        url = '{api_url}/{api_version}/order/{order_id}/'.format(
            api_url=self.API_URL,
            api_version=self.CLIENT_API_VERSION,
            order_id=order_id,
        )
        order = self._request('DELETE', url)
        return order
