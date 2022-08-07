# coding=utf-8

from Exchange import Exchange

class Binance(Exchange):
    def __init__(self, a):
        print(a)

    def get_exchange_info(self):
        print("is binance")