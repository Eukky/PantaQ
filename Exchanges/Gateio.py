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

    def set_simulation(self, is_sim):
        if is_sim:
            self.host = "https://fx-api-testnet.gateio.ws"
        else:
            self.host = "https://api.gateio.ws"

    def __gen_sign(self, method, url, query_string, payload_string):
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

    def get_future_order_book(self, settle, contract, interval, limit, with_id):
        self.url = '/futures/' + str(settle) + '/order_book'
        self.query_param = 'contract=' + str(contract)
        if interval:
            self.query_param += '&' + 'interval=' + str(interval)
        if limit:
            self.query_param += '&' + 'limit=' + str(limit)
        if with_id:
            self.query_param += '&' + 'with_id=' + str("true")
        r = requests.request('GET', self.host + self.prefix + self.url + "?" + self.query_param,
                             headers=self.common_headers)
        return r.json()

    def get_future_trades(self, settle, contract, limit, last_id, start_time, end_time):
        self.url = '/futures/' + str(settle) + '/trades'
        self.query_param = 'contract=' + str(contract)
        if limit:
            self.query_param += '&' + 'limit=' + str(limit)
        if last_id:
            self.query_param += '&' + 'last_id=' + str(last_id)
        if start_time:
            self.query_param += '&' + 'from=' + str(start_time)
        if end_time:
            self.query_param += '&' + 'to=' + str(end_time)
        r = requests.request('GET', self.host + self.prefix + self.url + "?" + self.query_param,
                             headers=self.common_headers)
        return r.json()

    def get_future_candlesticks(self, settle, contract, start_time, end_time, limit, interval):
        self.url = '/futures/' + str(settle) + '/candlesticks'
        self.query_param = 'contract=' + str(contract)
        if start_time:
            self.query_param += '&' + 'from=' + str(start_time)
        if end_time:
            self.query_param += '&' + 'to=' + str(end_time)
        if limit:
            self.query_param += '&' + 'limit=' + str(limit)
        if interval:
            self.query_param += '&' + 'interval=' + str(interval)
        r = requests.request('GET', self.host + self.prefix + self.url + "?" + self.query_param,
                             headers=self.common_headers)
        return r.json()

    def get_future_tickers(self, settle, contract):
        self.url = '/futures/' + str(settle) + '/tickers'
        self.query_param = ''
        if contract:
            self.query_param += 'contract=' + str(contract)
        r = requests.request('GET', self.host + self.prefix + self.url + "?" + self.query_param,
                             headers=self.common_headers)
        return r.json()

    def get_future_funding_rate(self, settle, contract, limit):
        self.url = '/futures/' + str(settle) + '/funding_rate'
        self.query_param = 'contract=' + str(contract)
        if limit:
            self.query_param += '&' + 'limit=' + str(limit)
        r = requests.request('GET', self.host + self.prefix + self.url + "?" + self.query_param,
                             headers=self.common_headers)
        return r.json()

    def get_future_insurance(self, settle, limit):
        self.url = '/futures/' + str(settle) + '/insurance'
        self.query_param = ''
        if limit:
            self.query_param += '&' + 'limit=' + str(limit)
        r = requests.request('GET', self.host + self.prefix + self.url + "?" + self.query_param,
                             headers=self.common_headers)
        return r.json()

    def get_future_contract_stats(self, settle, contract, start_time, interval, limit):
        self.url = '/futures/' + str(settle) + '/contract_stats'
        self.query_param = 'contract=' + str(contract)
        if start_time:
            self.query_param += '&' + 'from=' + str(start_time)
        if interval:
            self.query_param += '&' + 'interval=' + str(interval)
        if limit:
            self.query_param += '&' + 'limit=' + str(limit)
        r = requests.request('GET', self.host + self.prefix + self.url + "?" + self.query_param,
                             headers=self.common_headers)
        return r.json()

    def get_future_constituents(self, settle, index):
        self.url = '/futures/' + str(settle) + '/index_constituents/' + str(index)
        self.query_param = ''
        r = requests.request('GET', self.host + self.prefix + self.url + "?" + self.query_param,
                             headers=self.common_headers)
        return r.json()

    def get_future_liq_orders(self, settle, contract, start_time, end_time, limit):
        self.url = '/futures/' + str(settle) + '/liq_orders'
        self.query_param = ''
        if contract:
            self.query_param += 'contract=' + str(contract)
        if start_time:
            self.query_param += '&' + 'from=' + str(start_time)
        if end_time:
            self.query_param += '&' + 'to=' + str(end_time)
        if limit:
            self.query_param += '&' + 'limit=' + str(limit)
        r = requests.request('GET', self.host + self.prefix + self.url + "?" + self.query_param,
                             headers=self.common_headers)
        return r.json()

    def get_future_account_info(self, settle):
        self.url = '/futures/' + str(settle) + '/accounts'
        sign_headers = self.__gen_sign('GET', self.prefix + self.url, "", self.query_param)
        self.common_headers.update(sign_headers)
        r = requests.request('GET', self.host + self.prefix + self.url, headers=self.common_headers)
        return r.json()

    def get_future_account_book(self, settle, limit, start_time, end_time, type):
        self.url = '/futures/' + str(settle) + '/account_book'
        self.query_param = ''
        if limit:
            self.query_param += '&' + 'limit=' + str(limit)
        if start_time:
            self.query_param += '&' + 'from=' + str(start_time)
        if end_time:
            self.query_param += '&' + 'to=' + str(end_time)
        if type:
            self.query_param += '&' + 'type=' + str(type)
        sign_headers = self.__gen_sign('GET', self.prefix + self.url, "", self.query_param)
        self.common_headers.update(sign_headers)
        r = requests.request('GET', self.host + self.prefix + self.url, headers=self.common_headers)
        return r.json()

    def get_future_positions(self, settle):
        self.url = '/futures/' + str(settle) + '/positions'
        self.query_param = ''
        sign_headers = self.__gen_sign('GET', self.prefix + self.url, "", self.query_param)
        self.common_headers.update(sign_headers)
        r = requests.request('GET', self.host + self.prefix + self.url, headers=self.common_headers)
        return r.json()

    def get_future_contract_position(self, settle, contract):
        self.url = '/futures/' + str(settle) + '/positions/' + str(contract)
        self.query_param = ''
        sign_headers = self.__gen_sign('GET', self.prefix + self.url, "", self.query_param)
        self.common_headers.update(sign_headers)
        r = requests.request('GET', self.host + self.prefix + self.url, headers=self.common_headers)
        return r.json()

    def update_future_position_margin(self, settle, contract, change):
        self.url = '/futures/' + str(settle) + '/positions/' + str(contract) + "/margin"
        self.query_param = 'change=' + str(change)
        sign_headers = self.__gen_sign('POST', self.prefix + self.url, "", self.query_param)
        self.common_headers.update(sign_headers)
        r = requests.request('POST', self.host + self.prefix + self.url, headers=self.common_headers)
        return r.json()

    def update_future_position_leverage(self, settle, contract, leverage, cross_leverage_limit):
        self.url = '/futures/' + str(settle) + '/positions/' + str(contract) + "/leverage"
        self.query_param = 'leverage=' + str(leverage)
        if cross_leverage_limit:
            self.query_param += '&' + 'cross_leverage_limit=' + str(cross_leverage_limit)
        sign_headers = self.__gen_sign('POST', self.prefix + self.url, "", self.query_param)
        self.common_headers.update(sign_headers)
        r = requests.request('POST', self.host + self.prefix + self.url, headers=self.common_headers)
        return r.json()

    def update_future_position_risk_limit(self, settle, contract, risk_limit):
        self.url = '/futures/' + str(settle) + '/positions/' + str(contract) + "/risk_limit"
        self.query_param = 'risk_limit=' + str(risk_limit)
        sign_headers = self.__gen_sign('POST', self.prefix + self.url, "", self.query_param)
        self.common_headers.update(sign_headers)
        r = requests.request('POST', self.host + self.prefix + self.url, headers=self.common_headers)
        return r.json()

    def set_future_dual_mode(self, settle, dual_mode):
        self.url = '/futures/' + str(settle) + '/dual_mode'
        if dual_mode:
            self.query_param = 'dual_mode=true'
        else:
            self.query_param = 'dual_mode=false'
        sign_headers = self.__gen_sign('POST', self.prefix + self.url, "", self.query_param)
        self.common_headers.update(sign_headers)
        r = requests.request('POST', self.host + self.prefix + self.url, headers=self.common_headers)
        return r.json()

    def get_future_dual_comp_position(self, settle, contract):
        self.url = '/futures/' + str(settle) + '/dual_comp/positions/' + str(contract)
        self.query_param = ''
        sign_headers = self.__gen_sign('GET', self.prefix + self.url, "", self.query_param)
        self.common_headers.update(sign_headers)
        r = requests.request('GET', self.host + self.prefix + self.url, headers=self.common_headers)
        return r.json()

    def update_future_dual_comp_position_margin(self, settle, contract, change, dual_side):
        self.url = '/futures/' + str(settle) + '/dual_comp/positions/' + str(contract) + '/margin'
        self.query_param = 'change=' + str(change) + '&' + 'dual_side=' + str(dual_side)
        sign_headers = self.__gen_sign('POST', self.prefix + self.url, "", self.query_param)
        self.common_headers.update(sign_headers)
        r = requests.request('POST', self.host + self.prefix + self.url, headers=self.common_headers)
        return r.json()

    def update_future_dual_comp_position_leverage(self, settle, contract, leverage, cross_leverage_limit):
        self.url = '/futures/' + str(settle) + '/dual_comp/positions/' + str(contract) + '/leverage'
        self.query_param = 'leverage=' + str(leverage)
        if cross_leverage_limit:
            self.query_param += '&' + 'cross_leverage_limit=' + cross_leverage_limit
        sign_headers = self.__gen_sign('POST', self.prefix + self.url, "", self.query_param)
        self.common_headers.update(sign_headers)
        r = requests.request('POST', self.host + self.prefix + self.url, headers=self.common_headers)
        return r.json()

    def update_future_dual_comp_position_risk_limit(self, settle, risk_limit):
        self.url = '/futures/' + str(settle) + '/dual_comp/positions/' + str(contract) + '/risk_limit'
        self.query_param = 'risk_limit=' + str(risk_limit)
        sign_headers = self.__gen_sign('POST', self.prefix + self.url, "", self.query_param)
        self.common_headers.update(sign_headers)
        r = requests.request('POST', self.host + self.prefix + self.url, headers=self.common_headers)
        return r.json()

    def set_future_orders(self, settle, contract, size, iceberg, price, close, reduce_only, tif, text, auto_size):
        self.url = '/futures/' + str(settle) + '/orders'
        self.query_param = ''
        data = {}
        data['contract'] = str(contract)
        data['size'] = str(size)
        if iceberg:
            data['iceberg'] = str(iceberg)
        if price:
            data['price'] = str(price)
        if close:
            data['close'] = str(close)
        if reduce_only:
            data['reduce_only'] = str(reduce_only)
        if tif:
            data['tif'] = str(tif)
        if text:
            data['text'] = str(text)
        if auto_size:
            data['auto_size'] = str(auto_size)
        body = json.dumps(data)
        sign_headers = self.__gen_sign('POST', self.prefix + self.url, self.query_param, body)
        self.common_headers.update(sign_headers)
        r = requests.request('POST', self.host + self.prefix + self.url, headers=self.common_headers)
        return r.json()

    def get_future_orders(self, settle, contract, status, limit, offset, last_id, count_total):
        self.url = '/futures/' + str(settle) + '/orders'
        self.query_param = 'contract=' + str(contract) + '&' + 'status=' + str(status)
        if limit:
            self.query_param += '&' + 'limit=' + str(limit)
        if offset:
            self.query_param += '&' + 'offset=' + str(offset)
        if last_id:
            self.query_param += '&' + 'last_id=' + str(last_id)
        if count_total:
            self.query_param += '&' + 'count_total=' + str(count_total)
        sign_headers = self.__gen_sign('GET', self.prefix + self.url, "", self.query_param)
        self.common_headers.update(sign_headers)
        r = requests.request('GET', self.host + self.prefix + self.url, headers=self.common_headers)
        return r.json()

    def cancel_future_orders(self, settle, contract, side):
        self.url = '/futures/' + str(settle) + '/orders'
        self.query_param = 'contract=' + str(contract)
        sign_headers = self.__gen_sign('DELETE', self.prefix + self.url, "", self.query_param)
        self.common_headers.update(sign_headers)
        r = requests.request('DELETE', self.host + self.prefix + self.url, headers=self.common_headers)
        return r.json()

    def make_future_orders(self, orders, contract, size, iceberg, price, close, reduce_only, tif, text, auto_size):
        order = {'contract': str(contract), 'size': str(size)}
        if iceberg:
            order['iceberg'] = str(iceberg)
        if price:
            order['price'] = str(price)
        if close:
            order['close'] = str(close)
        if reduce_only:
            order['reduce_only'] = str(reduce_only)
        if tif:
            order['tif'] = str(tif)
        if text:
            order['text'] = str(text)
        if auto_size:
            order['auto_size'] = str(auto_size)
        orders.append(order)
        return json.dumps(order)

    def set_future_batch_orders(self, settle, orders):
        self.url = '/futures/' + str(settle) + '/batch_orders'
        self.query_param = ''
        body = []
        for order in orders:
            data = {'contract': str(order['contract']), 'size': str(order['size'])}
            if 'iceberg' in order:
                data['iceberg'] = str(order['iceberg'])
            if 'price' in order:
                data['price'] = str(order['price'])
            if 'close' in order:
                data['close'] = str(order['close'])
            if 'reduce_only' in order:
                data['reduce_only'] = str(order['reduce_only'])
            if 'tif' in order:
                data['tif'] = str(order['tif'])
            if 'text' in order:
                data['text'] = str(order['text'])
            if 'auto_size' in order:
                data['auto_size'] = str(order['auto_size'])
            body.append(json.dumps(data))
        sign_headers = self.__gen_sign('POST', self.prefix + self.url, self.query_param, body)
        self.common_headers.update(sign_headers)
        r = requests.request('POST', self.host + self.prefix + self.url, headers=self.common_headers)
        return r.json()

    def get_future_orders_with_id(self, settle, order_id):
        self.url = '/futures/' + str(settle) + '/orders/' + str(order_id)
        self.query_param = ''
        sign_headers = self.__gen_sign('GET', self.prefix + self.url, "", self.query_param)
        self.common_headers.update(sign_headers)
        r = requests.request('GET', self.host + self.prefix + self.url, headers=self.common_headers)
        return r.json()

    def cancel_future_orders_with_id(self, settle, order_id):
        self.url = '/futures/' + str(settle) + '/orders/' + str(order_id)
        self.query_param = ''
        sign_headers = self.__gen_sign('DELETE', self.prefix + self.url, "", self.query_param)
        self.common_headers.update(sign_headers)
        r = requests.request('DELETE', self.host + self.prefix + self.url, headers=self.common_headers)
        return r.json()

    def update_future_orders_with_id(self, settle, order_id, size, price):
        self.url = '/futures/' + str(settle) + '/orders/' + str(order_id)
        self.query_param = ''
        data = {}
        data['size'] = size
        data['price'] = price
        body = json.dumps(data)
        sign_headers = self.__gen_sign('PUT', self.prefix + self.url, "", self.query_param)
        self.common_headers.update(sign_headers)
        r = requests.request('PUT', self.host + self.prefix + self.url, headers=self.common_headers)
        return r.json()

    def get_future_my_trades(self, settle, contract, order, limit, offset, last_id, count_total):
        self.url = '/futures/' + str(settle) + '/my_trades'
        self.query_param = ''
        if contract:
            self.query_param += 'contract=' + str(contract)
        if order:
            self.query_param += '&' + 'order=' + str(order)
        if limit:
            self.query_param += '&' + 'limit=' + str(limit)
        if offset:
            self.query_param += '&' + 'offset=' + str(offset)
        if last_id:
            self.query_param += '&' + 'last_id=' + str(last_id)
        if count_total:
            self.query_param += '&' + 'count_total=' + str(count_total)
        sign_headers = self.__gen_sign('GET', self.prefix + self.url, "", self.query_param)
        self.common_headers.update(sign_headers)
        r = requests.request('GET', self.host + self.prefix + self.url, headers=self.common_headers)
        return r.json()

    def get_future_position_close(self, settle, contract, limit, offset, start_time, end_time):
        self.url = '/futures/' + str(settle) + '/position_close'
        self.query_param = ''
        if contract:
            self.query_param += 'contract=' + str(contract)
        if limit:
            self.query_param += '&' + 'limit=' + str(limit)
        if offset:
            self.query_param += '&' + 'offset=' + str(offset)
        if start_time:
            self.query_param += '&' + 'from=' + str(start_time)
        if end_time:
            self.query_param += '&' + 'to=' + str(end_time)
        sign_headers = self.__gen_sign('GET', self.prefix + self.url, "", self.query_param)
        self.common_headers.update(sign_headers)
        r = requests.request('GET', self.host + self.prefix + self.url, headers=self.common_headers)
        return r.json()

    def get_future_liquidates(self, settle, contract, limit, at_time):
        self.url = '/futures/' + str(settle) + '/liquidates'
        self.query_param = ''
        if contract:
            self.query_param += 'contract=' + str(contract)
        if limit:
            self.query_param += '&' + 'limit=' + str(limit)
        if at_time:
            self.query_param += '&' + 'at=' + str(at_time)
        sign_headers = self.__gen_sign('GET', self.prefix + self.url, "", self.query_param)
        self.common_headers.update(sign_headers)
        r = requests.request('GET', self.host + self.prefix + self.url, headers=self.common_headers)
        return r.json()

    def set_future_price_orders(self, settle, contract, price, size, close, tif, text, reduce_only, auto_size,
                                strategy_type, price_type, trigger_price, rule, expiration, order_type):
        self.url = '/futures/' + str(settle) + '/price_orders'
        self.query_param = ''
        initial = {}
        initial['contract'] = contract
        initial['price'] = price
        if size:
            initial['size'] = size
        if close:
            initial['close'] = close
        if tif:
            initial['tif'] = tif
        if text:
            initial['text'] = text
        if reduce_only:
            initial['reduce_only'] = reduce_only
        if auto_size:
            initial['auto_size'] = auto_size
        trigger = {}
        if strategy_type:
            initial['strategy_type'] = strategy_type
        if price_type:
            initial['price_type'] = price_type
        if trigger_price:
            initial['price'] = trigger_price
        if rule:
            initial['rule'] = rule
        if expiration:
            initial['expiration'] = expiration
        if order_type:
            order_type['order_type'] = order_type
        data = {initial, trigger, order_type}
        body = json.dumps(data)
        sign_headers = self.__gen_sign('POST', self.prefix + self.url, "", self.query_param)
        self.common_headers.update(sign_headers)
        r = requests.request('POST', self.host + self.prefix + self.url, headers=self.common_headers)
        return r.json()
        return

    def get_future_price_orders(self, settle, status, contract, limit, offset):
        self.url = '/futures/' + str(settle) + '/price_orders'
        self.query_param = 'status=' + str(status)
        if contract:
            self.query_param += '&' + 'contract=' + str(contract)
        if limit:
            self.query_param += '&' + 'limit=' + str(limit)
        if offset:
            self.query_param += '&' + 'offset=' + str(offset)
        sign_headers = self.__gen_sign('GET', self.prefix + self.url, "", self.query_param)
        self.common_headers.update(sign_headers)
        r = requests.request('GET', self.host + self.prefix + self.url, headers=self.common_headers)
        return r.json()

    def cancel_future_price_orders(self, settle, contract):
        self.url = '/futures/' + str(settle) + '/price_orders'
        self.query_param = 'contract=' + str(contract)
        sign_headers = self.__gen_sign('DELETE', self.prefix + self.url, "", self.query_param)
        self.common_headers.update(sign_headers)
        r = requests.request('DELETE', self.host + self.prefix + self.url, headers=self.common_headers)
        return r.json()

    def get_future_price_orders_with_id(self, settle, order_id):
        self.url = '/futures/' + str(settle) + '/price_orders/' + str(order_id)
        self.query_param = ''
        sign_headers = self.__gen_sign('GET', self.prefix + self.url, "", self.query_param)
        self.common_headers.update(sign_headers)
        r = requests.request('GET', self.host + self.prefix + self.url, headers=self.common_headers)
        return r.json()

    def cancel_future_price_orders_with_id(self, settle, order_id):
        self.url = '/futures/' + str(settle) + '/price_orders/' + str(order_id)
        self.query_param = ''
        sign_headers = self.__gen_sign('DELETE', self.prefix + self.url, "", self.query_param)
        self.common_headers.update(sign_headers)
        r = requests.request('DELETE', self.host + self.prefix + self.url, headers=self.common_headers)
        return r.json()
