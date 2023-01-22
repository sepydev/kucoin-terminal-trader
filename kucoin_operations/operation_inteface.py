from abc import ABC, abstractmethod

import kucoin.client


class IOperation(ABC):
    @abstractmethod
    def validate(self, **kwargs):
        pass

    @abstractmethod
    def execute(self, kucoin_client: kucoin.client.Market, trade_client: kucoin.client.Trade, **kwargs):
        pass
