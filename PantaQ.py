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

    def set_simulation(self, is_sim):
        self.exchange.set_simulation(is_sim)

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

    def get_future_order_book(self, settle, contract, interval=None, limit=None, with_id=None):
        return self.exchange.get_future_order_book(settle, contract, interval, limit, with_id)

    def get_future_trades(self, settle, contract, limit=None, last_id=None, start_time=None, end_time=None):
        return self.exchange.get_future_trades(settle, contract, limit, last_id, start_time, end_time)

    def get_future_candlesticks(self, settle, contract, start_time=None, end_time=None, limit=None, interval=None):
        return self.exchange.get_future_candlesticks(settle, contract, start_time, end_time, limit, interval)

    def get_future_tickers(self, settle, contract=None):
        return self.exchange.get_future_tickers(settle, contract)

    def get_future_funding_rate(self, settle, contract, limit=None):
        return self.exchange.get_future_funding_rate(settle, contract, limit)

    def get_future_insurance(self, settle, limit=None):
        return self.exchange.get_future_insurance(settle, limit)

    def get_future_contract_stats(self, settle, contract, start_time=None, interval=None, limit=None):
        return self.exchange.get_future_contract_stats(settle, contract, start_time, interval, limit)

    def get_future_constituents(self, settle, index):
        return self.exchange.get_future_constituents(settle, index)

    def get_future_liq_orders(self, settle, contract=None, start_time=None, end_time=None, limit=None):
        return self.exchange.get_future_liq_orders(settle, contract, start_time, end_time, limit)

    def get_future_account_info(self, settle):
        return self.exchange.get_future_account_info(settle)

    def get_future_account_book(self, settle, limit=None, start_time=None, end_time=None, type=None):
        return self.exchange.get_future_account_book(settle, limit, start_time, end_time, type)

    def get_future_positions(self, settle):
        return self.exchange.get_future_positions(settle)

    def get_future_contract_position(self, settle, contract):
        return self.exchange.get_future_contract_position(settle, contract)

    def update_future_position_margin(self, settle, contract, change):
        return self.exchange.update_future_position_margin(settle, contract, change)

    def update_future_position_leverage(self, settle, contract, leverage, cross_leverage_limit=None):
        return self.exchange.update_future_position_leverage(settle, contract, leverage, cross_leverage_limit)

    def update_future_position_risk_limit(self, settle, contract, risk_limit):
        return self.exchange.update_future_position_risk_limit(settle, contract, risk_limit)

    def set_future_dual_mode(self, settle, dual_mode):
        return self.exchange.set_future_dual_mode(settle, dual_mode)

    def get_future_dual_comp_position(self, settle, contract):
        return self.exchange.get_future_dual_comp_position(settle, contract)

    def update_future_dual_comp_position_margin(self, settle, contract, change, dual_side):
        return self.exchange.update_future_dual_comp_position_margin(settle, contract, change, dual_side)

    def update_future_dual_comp_position_leverage(self, settle, contract, leverage, cross_leverage_limit=None):
        return self.exchange.update_future_dual_comp_position_leverage(settle, contract, leverage, cross_leverage_limit)

    def update_future_dual_comp_position_risk_limit(self, settle, risk_limit):
        return self.exchange.update_future_dual_comp_position_risk_limit(settle, risk_limit)

    def set_future_orders(self, settle, contract, size, iceberg=None, price=None, close=None, reduce_only=None,
                          tif=None, text=None, auto_size=None):
        return self.exchange.set_future_orders(settle, contract, size, iceberg, price, close, reduce_only, tif, text,
                                               auto_size)

    def get_future_orders(self, settle, contract, status, limit=None, offset=None, last_id=None, count_total=None):
        return self.exchange.get_future_orders(settle, contract, status, limit, offset, last_id, count_total)

    def cancel_future_orders(self, settle, contract):
        return self.exchange.cancel_future_orders(settle, contract)

    def make_future_orders(self, orders, contract, size, iceberg=None, price=None, close=None, reduce_only=None,
                           tif=None, text=None, auto_size=None):
        return self.exchange.make_future_orders(orders, contract, size, iceberg, price, close, reduce_only, tif, text,
                                                auto_size)

    def set_future_batch_orders(self, settle, orders):
        return self.exchange.set_future_batch_orders(settle, orders)

    def get_future_orders_with_id(self, settle, order_id):
        return self.exchange.get_future_orders_with_id(settle, order_id)

    def cancel_future_orders_with_id(self, settle, order_id):
        return self.exchange.cancel_future_orders_with_id(settle, order_id)

    def update_future_orders_with_id(self, settle, order_id, size, price):
        return self.exchange.update_future_orders_with_id(settle, order_id, size, price)

    def get_future_my_trades(self, settle, contract=None, order=None, limit=None, offset=None, last_id=None,
                             count_total=None):
        return self.exchange.get_future_my_trades(settle, contract, order, limit, offset, last_id, count_total)

    def get_future_position_close(self, settle, contract=None, limit=None, offset=None, start_time=None, end_time=None):
        return self.exchange.get_future_position_close(settle, contract, limit, offset, start_time, end_time)

    def get_future_liquidates(self, settle, contract=None, limit=None, at_time=None):
        return self.exchange.get_future_liquidates(settle, contract, limit, at_time)

    def set_future_price_orders(self, settle, contract, price, size=None, close=None, tif=None, text=None,
                                reduce_only=None, auto_size=None, strategy_type=None, price_type=None,
                                trigger_price=None, rule=None, expiration=None, order_type=None):
        return self.exchange.set_future_price_orders(settle, contract, size, price, close, tif, text, reduce_only,
                                                     auto_size, strategy_type, price_type, trigger_price, rule,
                                                     expiration, order_type)

    def get_future_price_orders(self, settle, status, contract=None, limit=None, offset=None):
        return self.exchange.get_future_price_orders(settle, status, contract, limit, offset)

    def cancel_future_price_orders(self, settle, contract):
        return self.exchange.cancel_future_price_orders(settle, contract)

    def get_future_price_orders_with_id(self, settle, order_id):
        return self.exchange.get_future_price_orders_with_id(settle, order_id)

    def cancel_future_price_orders_with_id(self, settle, order_id):
        return self.exchange.cancel_future_price_orders_with_id(settle, order_id)
