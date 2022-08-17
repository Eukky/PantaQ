import sys

sys.path.append("..")

import PantaQ
import Config

if __name__ == "__main__":
    config = Config.Config()

    key = config.gateio.key_sim
    secret = config.gateio.secret_sim

    p = PantaQ.PantaQ("gateio")
    p.set_simulation(True)
    p.get_exchange_info()
    p.set_apikey(key, secret)

    settle = "usdt"
    contract = "BTC_USDT"

    # print(p.get_sever_time())

    # print(p.get_future_order_book(settle, contract))

    account_info = p.get_future_account_info(settle)
    future_info = p.get_future_info(settle, contract)
    funding_rate = p.get_future_funding_rate(settle, contract)
    maker_fee_rate = future_info['maker_fee_rate']
    taker_fee_rate = future_info['taker_fee_rate']
    # print(maker_fee_rate)
    # print(taker_fee_rate)

    candlesticks = p.get_future_candlesticks(settle, contract, limit=30, interval="1d")
    print(candlesticks)

    # settle = "usdt"
    # all_future_info = p.get_all_future_info(settle)
    # print(all_future_info)

    # fp = open("result.json","a+")
    # print(account_info, file=fp)
    # fp.close()
