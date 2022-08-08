# coding=utf-8

from Exchanges import Gateio
from Exchanges import Binance

class PantaQ():

    def __init__(self, exchange):
        self.exchange_name = exchange
        if exchange == "gateio":
            self.exchange = Gateio.Gateio()
        elif exchange == "binance":
            self.exchange = Binance.Binance()

    def get_support_exchanges(self):
        print("gateio, binance")

    def set_apikey(self, key, secret):
        self.exchange.set_apikey(key, secret)

    def ping(self):
        self.exchange.ping() 

    def get_sever_time(self):
        self.exchange.get_sever_time()

    def get_exchange_info(self):
        self.exchange.get_exchange_info()

    def get_account_info(self):
        self.exchange.get_account_info()
    

if __name__ == "__main__":
    p = PantaQ("gateio")
    p.get_exchange_info()

    key = ''        # api_key
    secret = '' 
    p.set_apikey(key, secret)
    p.get_account_info()
    