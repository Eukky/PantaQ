# coding=utf-8

import time
import hashlib
import hmac
import requests
import json
from .Exchange import Exchange

class Gateio(Exchange):
    def __init__(self):
        self.info = "gateio"
        self.host = "https://api.gateio.ws"
        self.prefix = "/api/v4"
        self.common_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        self.url = ''
        self.api = ''
        self.secret = ''
        self.query_param = ''
        self.body = {}
        
    def set_apikey(self, api, secret):
        self.api = api
        self.secret = secret

    def __gen_sign(self, method, url, query_string=None, payload_string=None):
        t = time.time()
        m = hashlib.sha512()
        m.update((payload_string or "").encode('utf-8'))
        hashed_payload = m.hexdigest()
        s = '%s\n%s\n%s\n%s\n%s' % (method, url, query_string or "", hashed_payload, t)
        sign = hmac.new(self.secret.encode('utf-8'), s.encode('utf-8'), hashlib.sha512).hexdigest()
        return {'KEY': self.api, 'Timestamp': str(t), 'SIGN': sign}

    def get_exchange_info(self):
        return self.info

############################################
### future api
############################################

    def get_future_account_info(self):
        self.url = '/futures/usdt/accounts'
        sign_headers = self.__gen_sign('GET', self.prefix + self.url, "", self.query_param)
        self.common_headers.update(sign_headers)
        r = requests.request('GET', self.host + self.prefix + self.url, headers=self.common_headers)
        return r.json()

    def get_all_future_info(self, settle):
        pass
    
    def get_future_info(self, settle, contract):
        pass

    def get_future_order_book(self, settle, contract, interval, limit, id):
        pass

    def get_future_trades(self, settle, contract, limit, last_id, start_time, end_time):
        pass

    def get_future_candlesticks(self, settle, contract, start_time, end_time, limit, interval):
        pass

    def get_future_tickers(self, settle, contract):
        pass