import kucoin
import pandas as pd
import ta

from kucoin_operations.operation_inteface import IOperation


class GetCandle(IOperation):
    def validate(self, **kwargs):
        market = kwargs.get('market')
        time_frame = kwargs.get('time_frame')
        if market is None or time_frame is None:
            raise ValueError("Missing market or time_frame argument")
        return True

    def execute(self, kucoin_client: kucoin.client.Market, trade_client: kucoin.client.Trade, **kwargs):
        if self.validate(**kwargs):
            market = kwargs.get('market')
            time_frame = kwargs.get('time_frame')
            kline_data = kucoin_client.get_candle(market, time_frame)
            kline_data = pd.DataFrame(kline_data, columns=["time", "open", "high", "low", "close", "volume"])
            kline_data['time'] = pd.to_datetime(kline_data['time'], unit='ms')
            kline_data = kline_data.set_index('time')
            kline_data['MA'] = kline_data['close'].rolling(window=5).mean()
            kline_data['EMA'] = kline_data['close'].ewm(span=5).mean()
            kline_data['RSI'] = ta.RSI(kline_data['close'], timeperiod=5)
            return kline_data
