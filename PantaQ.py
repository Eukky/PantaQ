# coding=utf-8

from Exchanges import Gateio
from Exchanges import Binance

import json

class PantaQ():

    def __init__(self, exchange):
        self.exchange_name = exchange
        self.support_exchanges = ['gateio', 'binance']
        if exchange == "gateio":
            self.exchange = Gateio.Gateio()
        elif exchange == "binance":
            self.exchange = Binance.Binance()

    def get_support_exchanges(self):
       return self.support_exchanges

    def set_apikey(self, key, secret):
        self.exchange.set_apikey(key, secret)

    def ping(self):
        self.exchange.ping() 

    def get_sever_time(self):
        return self.exchange.get_sever_time()

    def get_exchange_info(self):
        return self.exchange.get_exchange_info()

    def get_account_info(self):
        return self.exchange.get_account_info()
    

if __name__ == "__main__":
    p = PantaQ("gateio")
    p.get_exchange_info()

    key = ''        # api_key
    secret = '' 
    p.set_apikey(key, secret)
    account_info = p.get_account_info()
    print(account_info)
    # fp = open("result.json","a+")
    # print(account_info, file=fp)
    # fp.close() 