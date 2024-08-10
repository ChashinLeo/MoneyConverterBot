import requests
import json
from config import keys

class APIException(Exception):
    pass
class Converter:
    @staticmethod
    def get_price(base:str, quote:str, amount:str):

        if base == quote:
            raise APIionException('Вы указали одинаковые валюты!')
# Проверка верно введенной валюты
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}.')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}.')

# Проверка верно введенного кол-ва
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}.')
        if amount <= 0:
            raise APIException(f'Невозможно конверстировать количество валюты меньше или равное 0')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        total_quote = json.loads(r.content)[keys[quote]]
        total_quote = total_quote * amount

        return total_quote

