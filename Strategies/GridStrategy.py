# coding=utf-8
from enum import Enum
import json
import configparser

from Strategy import Strategy
from Exchanges.Exchange import Exchange
from Analyze import CandlestickIndicator


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
        # 主货币
        self._settle: str = ''
        # 交易品种
        self._contract: str = ''
        # 总投资额
        self._total_fund: float = 0
        # 杠杆倍数
        self._leverage: int = 0

        # 停止次数
        self._stop_count: int = 0
        # 目前次数
        self._current_count = 0
        # 停止时限
        self._stop_time: int = 0
        # 开始时间
        self._start_time = 0

        # 开单上限
        self._top_price: float = 0
        # 开单下限
        self._bottle_price: float = 0
        # 网格数量
        self._grid_num: int = 0
        # 等差价差
        self._equal_difference: float = 0
        # 等比比例
        self._equal_ratio: float = 0
        # 单格最高盈利
        self._max_profit: float = 0
        # 单格最低盈利
        self._min_profit: float = 0
        # 每格宽度
        self._grids_width = []

        # 止损上限
        self._top_stop_price: float = 0
        # 止损下限
        self._bottle_stop_price: float = 0
        # 止损比例上限
        self._top_stop_ratio: float = 0
        # 止损比例下限
        self._bottle_stop_ratio: float = 0

        self._exchange = None
        self._is_running = False
        self._grid_prices = []
        self._orders = []
        self._target_orders = []

    def load_config(self, path, section):
        config = configparser.ConfigParser()
        config.read(path, encoding="utf-8")

        if config.has_option(section, "strategy_type"):
            self._strategy_type = StrategyType(int(config.get(section, "strategy_type")))

        if self._strategy_type == StrategyType.NONE:
            print("please select strategy type: manual/auto")
            return

        if config.has_option(section, "grid_type"):
            self._grid_type = GridType(int(config.get(section, "grid_type")))
        else:
            print("please input grid_type:1-equal_difference/2-equal_ratio")
            return

        if config.has_option(section, "grid_side"):
            self._grid_side = GridSide(int(config.get(section, "grid_side")))
        else:
            print("please input grid_side:1-mid/2-up/3-down")
            return

        if config.has_option(section, "transaction_type"):
            self._transaction_type = TransactionType(int(config.get(section, "transaction_type")))
        else:
            print("please input transaction_type:1-spot/2-margin/3-futures")
            return

        if config.has_option(section, "settle"):
            self._settle = config.get(section, "settle")
        else:
            print("please input settle")
            return

        if config.has_option(section, "contract"):
            self._contract = config.get(section, "contract")
        else:
            print("please input contract")
            return

        if config.has_option(section, "total_fund"):
            self._total_fund = config.get(section, "total_fund")
        else:
            print("please input total_fund")
            return

        if config.has_option(section, "leverage"):
            self._leverage = config.get(section, "leverage")
        else:
            print("please input leverage")
            return

        if config.has_option(section, "stop_time"):
            self._stop_time = config.get(section, "stop_time")
        if config.has_option(section, "stop_count"):
            self._stop_count = config.get(section, "stop_count")
        if config.has_option(section, "top_stop_price"):
            self._top_stop_price = config.get(section, "top_stop_price")
        if config.has_option(section, "bottle_stop_price"):
            self._bottle_stop_price = config.get(section, "bottle_stop_price")
        if config.has_option(section, "top_stop_ratio"):
            self._top_stop_ratio = config.get(section, "top_stop_ratio")
        if config.has_option(section, "bottle_stop_ratio"):
            self._bottle_stop_ratio = config.get(section, "bottle_stop_ratio")

        if self._strategy_type == StrategyType.MANUAL:
            if self._grid_type == GridType.EQUAL_DIFFERENCE:
                if config.has_option(section, "equal_difference"):
                    self._equal_difference = config.get(section, "equal_difference")
                else:
                    print("please input equal_difference")
                    return
            elif self._grid_type == GridType.EQUAL_RATIO:
                if config.has_option(section, "equal_ratio"):
                    self._equal_difference = config.get(section, "equal_ratio")
                else:
                    print("please input equal_ratio")
                    return
            else:
                print("please select grid type: equal difference/equal ratio")
                return

    def export_config(self):
        pass

    def build_strategy(self):
        contract_info = self._exchange.get_future_info(self._settle, self._contract)
        taker_fee_rate = contract_info['taker_fee_rate']

        candlesticks = self._exchange.get_future_candlesticks(self._settle, self._contract, limit=30, interval="5m")

        self._exchange.set_future_dual_mode(self._settle, False)

        if self._strategy_type == StrategyType.AUTO:
            boll = CandlestickIndicator.BOLL()
            boll.calculate_bollinger_value(candlesticks)
            self._top_price = boll.get_up_band()[0]
            self._bottle_price = boll.get_down_band()[0]

        atr20 = CandlestickIndicator.ATR(20)
        atr20.calculate_atr(candlesticks)

        self._grid_num = int((self._top_price - self._bottle_price) / atr20.get_value())

        self._grid_prices = []
        if self._grid_type == GridType.EQUAL_DIFFERENCE:

            diff = (self._top_price - self._bottle_price) / self._grid_num
            self._equal_difference = diff

            for i in range(0, self._grid_num):
                price = self._bottle_price + i * diff
                self._grid_prices.append(price)

            self._max_profit = (self._grid_prices[1] / self._grid_prices[0]) - 1 - taker_fee_rate
            self._min_profit = (self._grid_prices[-1] / self._grid_prices[-2]) - 1 - taker_fee_rate

        elif self._grid_type == GridType.EQUAL_RATIO:

            ratio = pow(self._top_price / self._bottle_price, 1 / self._grid_num)
            self._equal_ratio = ratio

            for i in range(0, self._grid_num):
                price = self._bottle_price * pow(ratio, i)
                self._grid_prices.append(price)

            self._max_profit = ratio - taker_fee_rate
            self._min_profit = ratio - taker_fee_rate

        self._top_stop_price = min(self._top_stop_price, self._top_price * (1 + self._top_stop_ratio))
        self._bottle_stop_price = max(self._bottle_stop_price, self._bottle_price * (1 - self._bottle_stop_ratio))

    def execute_strategy(self):
        current_orders = self._exchange.get_future_orders(self._settle, self._contract)
        if current_orders:
            self._exchange.cancel_future_orders(self._settle, self._contract)

        self._start_time = self._exchange.get_sever_time()

        while self._is_running:
            contract_info = self._exchange.get_future_info(self._settle, self._contract)
            current_price = contract_info["mark_price"]

            if current_price < self._bottle_stop_price or current_price > self._top_stop_price:
                self.stop_strategy()

            current_time = self._exchange.get_sever_time()
            if current_time - self._start_time > self._stop_time:
                self.stop_strategy()

            if self._current_count > self._stop_count:
                self.stop_strategy()

            index = 0
            for i in range(0, self._grid_num):
                if self._grid_prices[i] > current_price:
                    index = i - 1

            current_down_price = self._grid_prices[index]
            current_up_price = self._grid_prices[index + 1]

            has_down_price_order = False
            has_up_price_order = False

            current_orders = self._exchange.get_future_orders(self._settle, self._contract)
            for order in current_orders:
                if order["price"] == current_down_price:
                    has_down_price_order = True
                if order["price"] == current_up_price:
                    has_up_price_order = True

            if not has_up_price_order:
                self._exchange.set_future_orders(self._settle, self._contract, price=current_up_price)
                self._current_count += 1
            if not has_down_price_order:
                self._exchange.set_future_orders(self._settle, self._contract, price=has_down_price_order)
                self._current_count += 1

    def stop_strategy(self):
        self._exchange.candel_future_orders(self._settle, self._contract)
        self._exchange.set_future_orders(self._settle, self._contract, size=0, price=0, close="true")
        return

    def set_exchange(self, exchange: Exchange):
        self._exchange = exchange

    def check_strategy(self):
        funding_rate = self._exchange.get_future_funding_rate(self._settle, self._contract)
        contract_info = self._exchange.get_future_info(self._settle, self._contract)
        maker_fee_rate = contract_info['maker_fee_rate']
        return
