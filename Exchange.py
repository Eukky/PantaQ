# coding=utf-8
from abc import ABCMeta, abstractclassmethod

class Exchange(metaclass=ABCMeta):
    def __init__(self, a):
        print(a)

    @abstractclassmethod
    def ping(self):
        pass 

    @abstractclassmethod
    def get_sever_time(self):
        pass

    @abstractclassmethod
    def get_account_info(self):
        pass

    @abstractclassmethod
    def get_exchange_info(self):
        pass