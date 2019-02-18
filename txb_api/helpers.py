# -*- coding: utf-8 -*-

from decimal import Decimal, ROUND_DOWN


def get_decimal_places(market: str) -> dict:
    markets = {
        'CREDITBTC': {
            'price': 2, 'quantity': 6, 'total': 8,
        },
        'CREDITETH': {
            'price': 2, 'quantity': 6, 'total': 8,
        },
        'CREDITLTC': {
            'price': 2, 'quantity': 6, 'total': 8,
        },
        'CREDITBCH': {
            'price': 2, 'quantity': 6, 'total': 8,
        },
        'CREDITBSV': {
            'price': 2, 'quantity': 6, 'total': 8,
        },
        'CREDITDASH': {
            'price': 2, 'quantity': 6, 'total': 8,
        },
        'CREDITNANO': {
            'price': 6, 'quantity': 6, 'total': 9,
        },
        'CREDITDOGE': {
            'price': 6, 'quantity': 6, 'total': 9,
        },
        'CREDITSMART': {
            'price': 6, 'quantity': 6, 'total': 9,
        },
        'CREDITZCR': {
            'price': 6, 'quantity': 6, 'total': 9,
        },
        'CREDITATMCASH': {
            'price': 6, 'quantity': 6, 'total': 9,
        },
        'CREDITLEAX': {
            'price': 6, 'quantity': 6, 'total': 9,
        },
        'CREDITTNJ': {
            'price': 6, 'quantity': 6, 'total': 9,
        },

        'BTCETH': {
            'price': 8, 'quantity': 6, 'total': 9,
        },
        'BTCLTC': {
            'price': 8, 'quantity': 6, 'total': 9,
        },
        'BTCBCH': {
            'price': 8, 'quantity': 6, 'total': 9,
        },
        'BTCBSV': {
            'price': 8, 'quantity': 6, 'total': 9,
        },
        'BTCDASH': {
            'price': 8, 'quantity': 6, 'total': 9,
        },
        'BTCNANO': {
            'price': 8, 'quantity': 6, 'total': 9,
        },
        'BTCDOGE': {
            'price': 9, 'quantity': 6, 'total': 9,
        },
        'BTCSMART': {
            'price': 9, 'quantity': 6, 'total': 9,
        },
        'BTCZCR': {
            'price': 8, 'quantity': 6, 'total': 9,
        },
        'BTCATMCASH': {
            'price': 9, 'quantity': 6, 'total': 9,
        },
        'BTCLEAX': {
            'price': 6, 'quantity': 6, 'total': 9,
        },
        'BTCTNJ': {
            'price': 8, 'quantity': 6, 'total': 9,
        },

        'DASHETH': {
            'price': 8, 'quantity': 6, 'total': 9,
        },
        'DASHLTC': {
            'price': 8, 'quantity': 6, 'total': 9,
        },
        'DASHBCH': {
            'price': 8, 'quantity': 6, 'total': 9,
        },
        'DASHBSV': {
            'price': 8, 'quantity': 6, 'total': 9,
        },
        'DASHNANO': {
            'price': 8, 'quantity': 6, 'total': 9,
        },
        'DASHDOGE': {
            'price': 9, 'quantity': 6, 'total': 9,
        },
        'DASHSMART': {
            'price': 9, 'quantity': 6, 'total': 9,
        },
        'DASHZCR': {
            'price': 9, 'quantity': 6, 'total': 9,
        },
        'DASHATMCASH': {
            'price': 9, 'quantity': 6, 'total': 9,
        },
        'DASHLEAX': {
            'price': 9, 'quantity': 6, 'total': 9,
        },
        'DASHTNJ': {
            'price': 9, 'quantity': 6, 'total': 9,
        },
    }
    return markets.get(market)


def format_decimal(value: Decimal, decimal_places: int = 8) -> Decimal:
    exp = Decimal(str('{0:.%sf}' % decimal_places).format(0))
    return value.quantize(exp, rounding=ROUND_DOWN)


def calc_order(market: str, unit_price: Decimal, quantity: Decimal = None,
               total: Decimal = None) -> (Decimal, Decimal, Decimal):
    if quantity:
        total = Decimal(str(unit_price)) * Decimal(str(quantity))
    else:
        quantity = Decimal(str(total)) / Decimal(str(unit_price))

    decimal_places = get_decimal_places(market)
    unit_price = format_decimal(unit_price, decimal_places.get('price'))
    quantity = format_decimal(quantity, decimal_places.get('quantity'))
    total = format_decimal(total, decimal_places.get('total'))
    return unit_price, quantity, total
