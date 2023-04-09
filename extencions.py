import json
import requests
from config import *



class ConvertException(Exception):
    pass



class ValuteConvertor:
    @staticmethod
    def convert(quote : str, base : str, amount : str):
    


        
        

        if quote == base:
            raise ConvertException('its odinakovo')

        try:
            quote_ticker = keys[quote]
        
        except KeyError:
            raise ConvertException(f'failed the procces,i dont understand this currency {quote}')
        
        try:
            base_ticker = keys[base]
        
        except KeyError:
            raise ConvertException(f'failed the procces,i dont understand this currency {base}')
        
        try:
            amount = float(amount)
        
        except ValueError:
            raise ConvertException(f'failed to process quantity, {amount}')

        quote_ticker, base_ticker = keys[quote], keys[base]
        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}")
        total_base = json.loads(r.content)[keys[base]]
        return total_base















