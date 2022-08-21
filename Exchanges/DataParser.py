# coding=utf-8

def parse_account_info(data, exchange):
    pass


def parse_contract_info(data, exchange_info):
    result = {}
    if exchange_info == "gateio":
        pass

    elif exchange_info == "binance":
        pass

    return result


def parse_candlesticks(data, exchange_info):
    result = []
    if exchange_info == "gateio":
        for item in data:
            new_item = {}
            for key, value in item.to_dict().items():
                if key == "c":
                    new_item["close"] = value
                if key == "h":
                    new_item["high"] = value
                if key == "l":
                    new_item["low"] = value
                if key == "o":
                    new_item["open"] = value
                if key == "t":
                    new_item["time"] = value
                if key == "v":
                    new_item["Volume"] = value
            result.append(new_item)
    elif exchange_info == "binance":
        pass
    return result

