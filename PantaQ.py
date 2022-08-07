# coding=utf-8

import Gateio
import Binance

class PantaQ():

    def __init__(self, exchange):
        self.exchange_name = exchange
        if exchange == "gateio":
            self.exchange = Gateio.Gateio(1)
        elif exchange == "binance":
            self.exchange = Binance.Binance(1)

    def get_support_exchanges(self):
        print("gateio, binance")

    def set_apikey(self, api, secret):
        self.api = api
        self.secret = secret

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