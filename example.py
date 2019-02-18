# -*- coding: utf-8 -*-

from decimal import Decimal

from txb_api.client import Client
from txb_api.public import Public

if __name__ == '__main__':
    txb_public = Public()
    txb_client = Client(client_id='<your_client_id>', client_secret='<your_client_secret>')

    ticker = txb_public.ticker()
    print(ticker)

    orderbook = txb_public.orderbook('CREDIT', 'BTC')
    print(orderbook)

    history = txb_public.market_history('CREDIT', 'BTC')
    print(history)

    balance = txb_client.balance()
    print(balance)

    unit_price = orderbook.get('buy_orders')[0].get('unit_price')
    order_buy = txb_client.create_order(
        order_type=txb_client.ORDER_BUY,
        currency_price='CREDIT', unit_price=Decimal(str(unit_price)),
        currency_quantity='BTC', percent_balance=100,
        execution_type=txb_client.ORDER_LIMIT,
    )
    print(order_buy)
