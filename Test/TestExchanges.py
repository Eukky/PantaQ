import sys

sys.path.append("..")

# import PantaQ
from Exchanges import Gateio
from Analyze import BaseStatistics
from Analyze import CandlestickIndicator

if __name__ == "__main__":
    settle = "usdt"
    contract = "BTC_USDT"
    g = Gateio.Gateio()
    g.load_config("../Configs/AccountConfig.ini", "GateioConfig")
    k = g.get_future_candlesticks(settle, contract)
    avg = BaseStatistics.average_for_candlesticks(k, "high")
    var = BaseStatistics.var_for_candlesticks(k, "low")
    std = BaseStatistics.std_for_candlesticks(k, "close")
    # print(avg)
    # print(var)
    # print(std)

    boll = CandlestickIndicator.BOLL()
    boll.calculate_bollinger_value(candlesticks=k)
    print(boll.get_up_band())
    print(boll.get_mid_band())
    print(boll.get_down_band())

    # p = PantaQ.PantaQ("gateio")
    # p.set_simulation(True)
    # p.get_exchange_info()
    #

    #
    # # print(p.get_sever_time())
    #
    # # print(p.get_future_order_book(settle, contract))
    #
    # account_info = p.get_future_account_info(settle)
    # future_info = p.get_future_info(settle, contract)
    # funding_rate = p.get_future_funding_rate(settle, contract)
    # maker_fee_rate = future_info['maker_fee_rate']
    # taker_fee_rate = future_info['taker_fee_rate']
    # # print(maker_fee_rate)
    # # print(taker_fee_rate)
    #
    # candlesticks = p.get_future_candlesticks(settle, contract, limit=30, interval="1d")
    # print(candlesticks)

    # settle = "usdt"
    # all_future_info = p.get_all_future_info(settle)
    # print(all_future_info)

    # fp = open("result.json","a+")
    # print(account_info, file=fp)
    # fp.close()
