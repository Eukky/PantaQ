# coding=utf-8
from . import BaseStatistics


class BOLL:
    def __init__(self):
        self._up_band = []
        self._mid_band = []
        self._down_band = []

    def calculate_bollinger_value(self, candlesticks: list):
        count = len(candlesticks)
        if count < 20:
            print("k线样本不足")

        for i in range(0, count - 20):
            time = candlesticks[i]["time"]
            mid_value = BaseStatistics.average_for_candlesticks(candlesticks[i:i+20], "close")
            up_value = mid_value + 2 * BaseStatistics.std_for_candlesticks(candlesticks[i:i+20], "close")
            down_value = mid_value - 2 * BaseStatistics.std_for_candlesticks(candlesticks[i:i+20], "close")

            self._mid_band.append({"mid": mid_value, "time": time})
            self._up_band.append({"up": up_value, "time": time})
            self._down_band.append({"down": down_value, "time": time})

    def get_up_band(self):
        return self._up_band

    def get_mid_band(self):
        return self._mid_band

    def get_down_band(self):
        return self._down_band


class ATR:
    def __init__(self, period: int):
        self._period = period
        self._value = 0

    def calculate_atr(self, candlesticks):
        count = len(candlesticks)
        if count < self._period:
            print("k线样本不足")
        atr = 0
        for num in range(1, count):
            last_tick = candlesticks[num - 1]
            tick = candlesticks[num]
            current_diff = tick['high'] - tick['low']
            last_high = abs(last_tick['close'] - tick['high'])
            last_low = abs(last_tick['close'] - tick['low'])
            tr = max(current_diff, last_low, last_high)
            atr += tr / count
        self._value = atr

    def get_value(self):
        return self._value

    def get_period(self):
        return self._period


class MA:
    def __init__(self):
        self._ma5 = []
        self._ma10 = []
        self._ma20 = []
        self._ma30 = []
        self._ma60 = []


class EMA:
    def __init__(self):
        pass


class MACD:
    def __init__(self):
        pass


class KDJ:
    def __init__(self):
        pass


class OHLC:
    def __init__(self):
        pass


class SAR:
    def __init__(self):
        pass



