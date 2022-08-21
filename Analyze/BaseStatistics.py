# coding=utf-8

import numpy as np


def average_for_candlesticks(candlesticks: list, key: str):
    close_sum = []
    for candlestick in candlesticks:
        close_sum.append(float(candlestick[key]))
    return np.average(close_sum)


def var_for_candlesticks(candlesticks: list, key: str):
    close_sum = []
    for candlestick in candlesticks:
        close_sum.append(float(candlestick[key]))
    return np.var(close_sum)


def std_for_candlesticks(candlesticks: list, key: str):
    close_sum = []
    for candlestick in candlesticks:
        close_sum.append(float(candlestick[key]))
    return np.std(close_sum)
