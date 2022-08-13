import sys
sys.path.append("..")

import PantaQ
import Config

if __name__ == "__main__":

    config = Config.Config()

    key = config.gateio.key
    secret = config.gateio.secret 

    p = PantaQ.PantaQ("gateio")
    p.get_exchange_info()
    p.set_apikey(key, secret)

    settle = "usdt"
    contract = "BTC_USDT"

    # print(p.get_sever_time())

    print(p.get_future_order_book(settle, contract))

    # account_info = p.get_account_info()
    # print(account_info)

    # settle = "usdt"
    # all_future_info = p.get_all_future_info(settle)
    # print(all_future_info)

    # fp = open("result.json","a+")
    # print(account_info, file=fp)
    # fp.close() 