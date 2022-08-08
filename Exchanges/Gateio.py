# coding=utf-8

import time
import hashlib
import hmac
import requests
import json
from .Exchange import Exchange

class Gateio(Exchange):
    def __init__(self):
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

    def gen_sign(self, method, url, query_string=None, payload_string=None):
        t = time.time()
        m = hashlib.sha512()
        m.update((payload_string or "").encode('utf-8'))
        hashed_payload = m.hexdigest()
        s = '%s\n%s\n%s\n%s\n%s' % (method, url, query_string or "", hashed_payload, t)
        sign = hmac.new(self.secret.encode('utf-8'), s.encode('utf-8'), hashlib.sha512).hexdigest()
        return {'KEY': self.api, 'Timestamp': str(t), 'SIGN': sign}

    def get_exchange_info(self):
        print("is gateio")

    def get_account_info(self):
        self.url = '/futures/usdt/accounts'
        self.body = {"contract": "BTC_USD", "size": 100, "price": "30", "tif": "gtc"}
        request_content = json.dumps(self.body)
        sign_headers = self.gen_sign('GET', self.prefix + self.url, "", self.query_param)
        self.common_headers.update(sign_headers)
        print('signature headers: %s' % sign_headers)
        # res = requests.post(host + prefix + url, headers=sign_headers, data=request_content)
        r = requests.request('GET', self.host + self.prefix + self.url, headers=self.common_headers)

        fp = open("result.json","a+")
        print(r.json(), file=fp)
        fp.close() 