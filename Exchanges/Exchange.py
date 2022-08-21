# coding=utf-8
from abc import ABCMeta, abstractmethod


class Exchange(metaclass=ABCMeta):

    def __init__(self):
        pass


    # 获取服务器时间
    @abstractmethod
    def get_sever_time(self):
        pass

    # 获取交易所信息
    @abstractmethod
    def get_exchange_info(self):
        pass

    # 查询该货币所有合约信息
    @abstractmethod
    def get_all_future_info(self, settle):
        pass

    # 查看单个合约信息
    @abstractmethod
    def get_future_info(self, settle, contract):
        pass

    # 查看订单深度信息
    @abstractmethod
    def get_future_order_book(self, settle, contract, interval, limit, with_id):
        pass

    # 查看成交记录
    @abstractmethod
    def get_future_trades(self, settle, contract, limit, last_id, start_time, end_time):
        pass

    # 查看k线
    @abstractmethod
    def get_future_candlesticks(self, settle, contract, start_time, end_time, limit, interval):
        pass

    # 查看合约交易行情统计
    @abstractmethod
    def get_future_tickers(self, settle, contract):
        pass

    # 查看合约时长历史资金费率
    @abstractmethod
    def get_future_funding_rate(self, settle, contract, limit):
        pass

    # 合约时长保险基金历史
    @abstractmethod
    def get_future_insurance(self, settle, limit):
        pass

    # 合约统计信息
    @abstractmethod
    def get_future_contract_stats(self, settle, contract, start_time, interval, limit):
        pass

    # 查询指数来源
    @abstractmethod
    def get_future_constituents(self, settle, index):
        pass

    # 查询强平委托历史
    @abstractmethod
    def get_future_liq_orders(self, settle, contract, start_time, end_time, limit):
        pass

    # 获取合约账号
    @abstractmethod
    def get_future_account_info(self, settle):
        pass

    # 查询合约账户变更历史
    @abstractmethod
    def get_future_account_book(self, settle, limit, start_time, end_time, type):
        pass

    # 获取仓位列表
    @abstractmethod
    def get_future_positions(self, settle):
        pass

    # 获取单个仓位信息
    @abstractmethod
    def get_future_contract_position(self, settle, contract):
        pass

    # 更新仓位保证金
    @abstractmethod
    def update_future_position_margin(self, settle, contract, change):
        pass

    # 更新仓位杠杆
    @abstractmethod
    def update_future_position_leverage(self, settle, contract, leverage, cross_leverage_limit):
        pass

    # 更新仓位风险限额
    @abstractmethod
    def update_future_position_risk_limit(self, settle, contract, risk_limit):
        pass

    # 设置持仓模式
    @abstractmethod
    def set_future_dual_mode(self, settle, dual_mode):
        pass

    # 获取双仓模式下的持仓信息
    @abstractmethod
    def get_future_dual_comp_position(self, settle, contract):
        pass

    # 更新双仓模式下的保证金
    @abstractmethod
    def update_future_dual_comp_position_margin(self, settle, contract, change, dual_side):
        pass

    # 更新双仓模式下的杠杆
    @abstractmethod
    def update_future_dual_comp_position_leverage(self, settle, contract, leverage, cross_leverage_limit):
        pass

    # 更新双仓模式下的风险限额
    @abstractmethod
    def update_future_dual_comp_position_risk_limit(self, settle, risk_limit):
        pass

    # 合约交易下单
    @abstractmethod
    def set_future_orders(self, settle, contract, size, iceberg, price, close, reduce_only, tif, text, auto_size):
        pass

    # 查询合约订单列表
    @abstractmethod
    def get_future_orders(self, settle, contract, status, limit, offset, last_id, count_total):
        pass

    # 批量取消状态为 open 的订单
    @abstractmethod
    def cancel_future_orders(self, settle, contract):
        pass

    # 创建订单
    @abstractmethod
    def make_future_orders(self, orders, contract, size, iceberg, price, close, reduce_only, tif, text, auto_size):
        pass

    # 合约交易批量下单
    @abstractmethod
    def set_future_batch_orders(self, settle, orders):
        pass

    # 查询单个订单详情
    @abstractmethod
    def get_future_orders_with_id(self, settle, order_id):
        pass

    # 撤销单个订单
    @abstractmethod
    def cancel_future_orders_with_id(self, settle, order_id):
        pass

    # 修改单个订单
    @abstractmethod
    def update_future_orders_with_id(self, settle, order_id, size, price):
        pass

    # 查询个人成交记录
    @abstractmethod
    def get_future_my_trades(self, settle, contract, order, limit, offset, last_id, count_total):
        pass

    # 查询平仓历史
    @abstractmethod
    def get_future_position_close(self, settle, contract, limit, offset, start_time, end_time):
        pass

    # 查询强制平仓历史
    @abstractmethod
    def get_future_liquidates(self, settle, contract, limit, at_time):
        pass

    # 创建价格触发订单
    @abstractmethod
    def set_future_price_orders(self, settle, contract, price, size, close, tif, text, reduce_only, auto_size,
                                strategy_type, price_type, trigger_price, rule, expiration, order_type):
        pass

    # 查询自动订单列表
    @abstractmethod
    def get_future_price_orders(self, settle, status, contract, limit, offset):
        pass

    # 批量取消自动订单
    @abstractmethod
    def cancel_future_price_orders(self, settle, contract):
        pass

    # 查询单个订单详情
    @abstractmethod
    def get_future_price_orders_with_id(self, settle, order_id):
        pass

    # 撤销单个自动订单
    @abstractmethod
    def cancel_future_price_orders_with_id(self, settle, order_id):
        pass
