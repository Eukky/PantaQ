class GateioConfig:
    def __init__(self):
        self.key = ''
        self.secret = ''
        self.key_sim = ''
        self.secret_sim = ''


class BinanaceConfig:
    def __init__(self):
        self.key = ''
        self.secret = ''


class Config:
    def __init__(self):
        self.gateio = GateioConfig()
        self.binance = BinanaceConfig()

