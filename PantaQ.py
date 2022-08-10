# coding=utf-8

from Exchanges import Gateio
from Exchanges import Binance

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

    def get_all_future_info(self, settle):
        return self.exchange.get_all_future_info(settle)
    
    def get_future_info(self, settle, contract):
        return self.exchange.get_future_info(settle, contract)
    
    def get_future_order_book(self, settle, contract, interval, limit, with_id):
        return self.exchange.get_future_order_book(settle, contract, interval, limit, with_id)

    def get_future_trades(self, settle, contract, limit, last_id, start_time, end_time):
        pass

    
    def get_future_candlesticks(self, settle, contract, start_time, end_time, limit, interval):
        pass

    
    def get_future_tickers(self, settle, contract):
        pass

    
    def get_future_funding_rate(self, settle, contract, limit):
        pass

    
    def get_future_insurance(self, settle, limit):
        pass
    
    
    def get_future_contract_stats(self, settle, contract, start_time, interval, limit):
        pass

    
    def get_future_constituents(self, settle, index):
        pass

    
    def get_future_liq_orders(self, settle, contract, start_time, end_time, limit):
        pass

    def get_future_account_info(self, settle):
        return self.exchange.get_account_info(settle)

    def get_future_account_book(self, settle, limit, start_time, end_time, type):
        pass

    
    def get_future_positions(self, settle):
        pass

    
    def get_future_contract_position(self, settle, contract):
        pass

    
    def update_future_position_margin(self, settle, contract, change):
        pass

    
    def update_future_position_leverage(self, settle, contract, leverage, cross_leverage_limit):
        pass

    
    def update_future_position_risk_limit(self, settle, contract, risk_limit):
        pass

    
    def set_future_dual_mode(self, settle, dual_mode):
        pass
    
    
    def get_future_dual_comp_position(self, settle, contract):
        pass

    
    def update_future_dual_comp_position_margin(self, settle, contract, change, dual_side):
        pass

    
    def update_future_dual_comp_position_leverage(self, settle, contract, leverage, cross_leverage_limit):
        pass

    
    def update_future_dual_comp_position_risk_limit(self, settle, risk_limit):
        pass

    
    def set_future_orders(self, settle, contract, size, iceberg, price, close, reduce_only, tif, text, auto_size):
        pass

    
    def get_future_orders(self, settle, contract, status, limit, offset, last_id, count_total):
        pass


    def cancle_future_orders(self, settle, contract, side):
        pass

    
    def set_future_batch_orders(self, settle, contract, size, iceberg, price, close, reduce_only, tif, text, auto_size):
        pass

    
    def get_future_orders_with_id(self, settle, order_id):
        pass

    
    def cancle_future_ofders_with_id(self, settle, order_id):
        pass

    
    def update_future_ofders_with_id(self, settle, order_id):
        pass
    
    
    def get_future_my_trades(self, settle, contract, order, limit, offset, last_id, count_total):
        pass

    
    def get_future_position_close(self, settle, contract, limit, offset, start_time, end_time):
        pass

    
    def get_future_liquidates(self, settle, contract, limit, at_time):
        pass
    
    
    def set_future_price_orders(self, settle, contract, size, price, close, tif, text, reduce_only, auto_size, strategy_type, price_type, rule, expiration, order_type):
        pass
    
    
    def get_future_price_orders(self, settle, contract, status, limit, offset):
        pass

    
    def cancle_future_price_orders(self, settle, contract):
        pass

    
    def get_future_price_orders_with_id(self, settle, order_id):
        pass

    
    def cancle_future_price_orders_with_id(self, settle, order_id):
        pass
    

