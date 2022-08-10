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

    def __gen_sign(self, method, url, query_string=None, payload_string=None):
        t = time.time()
        m = hashlib.sha512()
        m.update((payload_string or "").encode('utf-8'))
        hashed_payload = m.hexdigest()
        s = '%s\n%s\n%s\n%s\n%s' % (method, url, query_string or "", hashed_payload, t)
        sign = hmac.new(self.secret.encode('utf-8'), s.encode('utf-8'), hashlib.sha512).hexdigest()
        return {'KEY': self.api, 'Timestamp': str(t), 'SIGN': sign}


    def ping(self):
        return 

    def get_sever_time(self):
        self.url = '/spot/time'
        r = requests.request('GET', self.host + self.prefix + self.url, headers=self.common_headers)
        return r.json()

    def set_apikey(self, api, secret):
        self.api = api
        self.secret = secret

    def get_exchange_info(self):
        return self.info

    def get_all_future_info(self, settle):
        self.url = '/futures/' + str(settle) + '/contracts'
        r = requests.request('GET', self.host + self.prefix + self.url, headers=self.common_headers)
        return r.json()
    
    def get_future_info(self, settle, contract):
        self.url = '/futures/' + str(settle) + '/contracts/' + str(contract)
        r = requests.request('GET', self.host + self.prefix + self.url, headers=self.common_headers)
        return r.json()

    def get_future_order_book(self, settle, contract, interval=0, limit=0, with_id=False):
        self.url = '/futures/' + str(settle) + '/order_book'
        self.query_param = 'contract=' + str(contract) + '&' + 'interval=' + str(interval) + '&' + 'limit=' + str(limit)
        r = requests.request('GET', self.host + self.prefix + self.url + "?" + self.query_param, headers=self.common_headers)
        return r.json() 

    def get_future_trades(self, settle, contract, limit, last_id, start_time, end_time):
        return 

    def get_future_candlesticks(self, settle, contract, start_time, end_time, limit, interval):
        return 

    def get_future_tickers(self, settle, contract):
        return 

    def get_future_funding_rate(self, settle, contract, limit):
        return 

    
    def get_future_insurance(self, settle, limit):
        return 
    
    def get_future_contract_stats(self, settle, contract, start_time, interval, limit):
        return 
    
    def get_future_constituents(self, settle, index):
        return 

    def get_future_liq_orders(self, settle, contract, start_time, end_time, limit):
        return 

    def get_future_account_info(self, settle):
        self.url = '/futures/' + str(settle) +'/accounts'
        sign_headers = self.__gen_sign('GET', self.prefix + self.url, "", self.query_param)
        self.common_headers.update(sign_headers)
        r = requests.request('GET', self.host + self.prefix + self.url, headers=self.common_headers)
        return r.json()

    def get_future_account_book(self, settle, limit, start_time, end_time, type):
        return 

    
    def get_future_positions(self, settle):
        return 

    
    def get_future_contract_position(self, settle, contract):
        return 

    
    def update_future_position_margin(self, settle, contract, change):
        return 

    
    def update_future_position_leverage(self, settle, contract, leverage, cross_leverage_limit):
        return 

    
    def update_future_position_risk_limit(self, settle, contract, risk_limit):
        return 

    
    def set_future_dual_mode(self, settle, dual_mode):
        return 
    
    
    def get_future_dual_comp_position(self, settle, contract):
        return 

    
    def update_future_dual_comp_position_margin(self, settle, contract, change, dual_side):
        return 

    
    def update_future_dual_comp_position_leverage(self, settle, contract, leverage, cross_leverage_limit):
        return 

    
    def update_future_dual_comp_position_risk_limit(self, settle, risk_limit):
        return 

    
    def set_future_orders(self, settle, contract, size, iceberg, price, close, reduce_only, tif, text, auto_size):
        return 

    
    def get_future_orders(self, settle, contract, status, limit, offset, last_id, count_total):
        return 


    def cancle_future_orders(self, settle, contract, side):
        return 

    
    def set_future_batch_orders(self, settle, contract, size, iceberg, price, close, reduce_only, tif, text, auto_size):
        return 

    
    def get_future_orders_with_id(self, settle, order_id):
        return 

    
    def cancle_future_ofders_with_id(self, settle, order_id):
        return 

    
    def update_future_ofders_with_id(self, settle, order_id):
        return 
    
    
    def get_future_my_trades(self, settle, contract, order, limit, offset, last_id, count_total):
        return 

    
    def get_future_position_close(self, settle, contract, limit, offset, start_time, end_time):
        return 

    
    def get_future_liquidates(self, settle, contract, limit, at_time):
        return 
    
    
    def set_future_price_orders(self, settle, contract, size, price, close, tif, text, reduce_only, auto_size, strategy_type, price_type, rule, expiration, order_type):
        return 
    
    
    def get_future_price_orders(self, settle, contract, status, limit, offset):
        return 

    
    def cancle_future_price_orders(self, settle, contract):
        return 

    
    def get_future_price_orders_with_id(self, settle, order_id):
        return 

    
    def cancle_future_price_orders_with_id(self, settle, order_id):
        return 
    

