import kucoin
import pandas as pd
import talib as ta

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
            kline_data = kucoin_client.get_kline(market, time_frame)
            kline_data = pd.DataFrame(kline_data, columns=["time", "open", "close", "high", "low", "volume", "amount"])
            kline_data['time'] = pd.to_datetime(kline_data['time'], unit='s')
            kline_data = kline_data.set_index('time')
            kline_data = kline_data.sort_values('time',ascending=True)
            kline_data['MA'] = kline_data['close'].rolling(window=9).mean()
            kline_data['EMA'] = kline_data['close'].ewm(span=20).mean()
            kline_data['RSI'] = ta.RSI(kline_data['close'], timeperiod=14)
            return kline_data
