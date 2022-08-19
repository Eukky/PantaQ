# coding=utf-8
from enum import Enum
import json
import configparser

from Strategy import Strategy
from Exchanges.Exchange import Exchange


class StrategyType(Enum):
    NONE = 0
    MANUAL = 1
    AUTO = 2


class GridType(Enum):
    NONE = 0
    EQUAL_DIFFERENCE = 1
    EQUAL_RATIO = 2


class GridSide(Enum):
    NONE = 0
    MID = 1
    UP = 2
    DOWN = 3


class TransactionType(Enum):
    NONE = 0
    SPOT = 1
    MARGIN = 2
    FUTURES = 3


class OrderSide(Enum):
    NONE = 0
    MORE = 1
    LESS = 2


class GridStrategy(Strategy):

    def __init__(self):
        # 策略类型
        self._strategy_type = StrategyType.NONE
        # 网格类型
        self._grid_type = GridType.NONE
        # 策略倾向
        self._grid_side = GridSide.NONE
        # 交易种类
        self._transaction_type = TransactionType.NONE
        # 开单上限
        self._top_price: float = 0
        # 开单下限
        self._bottle_price: float = 0
        # 止损上限
        self._top_stop_price: float = 0
        # 止损下限
        self._bottle_stop_price: float = 0
        # 止损比例上限
        self._top_stop_ratio: float = 0
        # 止损比例下限
        self._bottle_stop_ratio: float = 0

        # 停止次数
        self._stop_count: int = 0
        # 停止时限
        self._stop_time: int = 0

        # 网格数量
        self._grid_num: int = 0
        # 等差价差
        self._equal_difference: float = 0
        # 等比比例
        self._equal_ratio: float = 0
        # 杠杆倍数
        self._leverage: int = 0
        # 每格盈利
        self._profit_per_grid: float = 0
        # 每格宽度
        self._grids_width = []

        # 总投资额
        self._total_fund: float = 0
        # 主货币
        self._settle: str = ''
        # 交易品种
        self._contract: str = ''

        self._exchange: Exchange = None
        self._is_running: bool = False
        self._orders: list = []
        self._target_orders: list = []

    def export_strategy(self):
        strategy_config = {'grid_type': str(self._grid_type), 'grid_side': str(self._grid_side),
                           'transaction_type': str(self._transaction_type), 'top_price': self._top_price,
                           'bottle_price': self._bottle_price, 'top_stop_price': self._top_stop_price,
                           'bottle_stop_price': self._bottle_stop_price, 'top_stop_ratio': self._top_stop_ratio,
                           'bottle_stop_ratio': self._bottle_stop_ratio, 'stop_count': self._stop_count,
                           'stop_time': self._stop_time, 'grid_num': self._grid_num,
                           'equal_difference': self._equal_difference, 'equal_ratio': self._equal_ratio,
                           'leverage': self._leverage, 'total_fund': self._total_fund, 'settle': self._settle,
                           'contract': self._contract}
        return json.dumps(strategy_config)

    def set_exchange(self, exchange: Exchange):
        self._exchange = exchange

    def check_strategy(self):
        funding_rate = self._exchange.get_future_funding_rate(self._settle, self._contract)
        contract_info = self._exchange.get_future_info(self._settle, self._contract)
        maker_fee_rate = contract_info['maker_fee_rate']
        return

    def calculate_atr(self, days: int):
        candlesticks = self._exchange.get_future_candlesticks(self._settle, self._contract, limit=days, interval="1d")
        count = candlesticks.len()
        atr = 0
        for num in range(1, count):
            last_tick = candlesticks[num - 1]
            tick = candlesticks[num]
            current_diff = tick['h'] - tick['l']
            last_high = abs(last_tick['c'] - tick['h'])
            last_low = abs(last_tick['c'] - tick['l'])
            tr = max(current_diff, last_low, last_high)
            atr += tr / count
        return atr

    def init_orders(self, prices: list):
        num = prices.len()
        for i in range(0, num):
            if i < num / 2:
                price = prices[i]
                order = {'price': price, 'side': OrderSide.MORE}
                self._orders.append(order)
                # 开买单
            else:
                # 开卖单
                price = prices[i]
                order = {'price': price, 'side': OrderSide.LESS}
                self._orders.append(order)

    def calculate_grids_width(self, taker_fee_rate):
        for order in self._orders:
            if order['side'] == OrderSide.MORE:
                target_price = order['price'] * (1 + (self._profit_per_grid - taker_fee_rate))
                width = target_price - order['price']
                self._grids_width.append(width)
                self._target_orders.append({'price': target_price, 'side': OrderSide.LESS})
            elif order['side'] == OrderSide.LESS:
                target_price = order['price'] * (1 - (self._profit_per_grid - taker_fee_rate))
                width = order['price'] - target_price
                self._grids_width.append(width)
                self._target_orders.append({'price': target_price, 'side': OrderSide.MORE})

    def execute_strategy(self):
        self._orders = []
        self._is_running = True

        # 查询合约目前的情况
        contract_info = self._exchange.get_future_info(self._settle, self._contract)
        contract_order_book = self._exchange.get_future_order_book(self._settle, self._contract)
        funding_rate = self._exchange.get_future_funding_rate(self._settle, self._contract)

        if self._strategy_type == StrategyType.AUTO:
            # 计算均值，布林线等指标
            # todo
            pass

        # 查询目前挂单
        if self._exchange:
            current_orders = self._exchange.get_future_orders(self._settle, self._contract)
        else:
            print("未设置指定交易所，策略终止")
            return

        # 如果已经有挂单，则取消挂单
        if current_orders:
            self._exchange.cancel_future_orders(self._settle, self._contract)

        # 计算ATR
        atr = self.calculate_atr(14)

        # 计算网格数量
        self._grid_num = int((self._top_price - self._bottle_price) / atr)

        # 计算网格价位
        prices = []
        if self._grid_type == GridType.EQUAL_DIFFERENCE:
            for i in range(0, self._grid_num):
                diff = (self._top_price - self._bottle_price) / self._grid_num
                self._equal_difference = diff
                price = self._bottle_price + i * diff
                prices.append(price)
        elif self._grid_type == GridType.EQUAL_RATIO:
            for i in range(0, self._grid_num):
                diff = pow(self._top_price / self._bottle_price, 1 / self._grid_num)
                self._equal_ratio = diff
                price = self._bottle_price * pow(diff, i)
                prices.append(price)
        else:
            print("请指定网格类型")
            return

        # 计算下单列表
        self.init_orders(prices)

        # 计算每格宽度
        taker_fee_rate = contract_info['taker_fee_rate']
        self.calculate_grids_width(taker_fee_rate)

        # 开单
        for order in self._orders:
            self._exchange.set_future_orders(self._settle, self._contract, price=order['price'])

        # 策略主循环
        self.strategy_loop()

    def strategy_loop(self):
        while self._is_running:
            # 查询目前挂单
            current_orders = self._exchange.get_future_orders(self._settle, self._contract)
            sorted_current_orders = sorted(current_orders, key=lambda orders: orders.get("price", 0))
            current_orders_num = current_orders.len()
            orders_num = self._orders.len()
            last_price = 0
            price_down = 0
            price_up = 0

            if current_orders_num < orders_num:
                for i in range(0, orders_num):
                    if sorted_current_orders[i]["price"] != self._orders[i]["price"]:
                        last_price = self._orders[i]["price"]
                        if i > 0:
                            price_down = self._orders[i - 1]["price"]
                        if i < orders_num - 1:
                            price_up = self._orders[i + 1]["price"]

                order_down =  {'price': price_down, 'side': OrderSide.MORE}
                order_up = {'price': price_up, 'side': OrderSide.LESS}
                if sorted_current_orders[i - 1] != order_down:
                    self._exchange.set_future_orders(self._settle, self._contract, price=price_down)

                if sorted_current_orders[i] != order_up:
                    self._exchange.set_future_orders(self._settle, self._contract, price=price_up)


if __name__ == "__main__":
    g = GridStrategy()
    print(g.export_strategy())
    config = configparser.ConfigParser()
    config.read("../Configs/AccountConfig.ini", encoding="utf-8")
    sec = config.sections()
    print(sec)

    grid_config = configparser.ConfigParser()
    grid_config.read("../Configs/GridStrategyConfig.ini", encoding="utf-8")
    grid_sec = grid_config.sections()
    items = grid_config.items(grid_sec[0])
    print(items)