import kucoin

from kucoin_operations.operation_inteface import IOperation


class CreateStopLossOrder(IOperation):
    def validate(self, **kwargs):
        market = kwargs.get('market')
        side = kwargs.get('side')
        price = kwargs.get('price')
        size = kwargs.get('size')
        stop_price = kwargs.get('stop_price')
        if any(map(lambda x: x is not None, [market, side, price, size, stop_price])):
            raise ValueError("Missing argument")
        return True

    def execute(self, kucoin_client: kucoin.client.Market, trade_client: kucoin.client.Trade, **kwargs):
        if self.validate(**kwargs):
            market = kwargs.get('market')
            side = kwargs.get('side')
            price = kwargs.get('price')
            size = kwargs.get('size')
            stop_price = kwargs.get('stop_price')
            return kucoin_client.create_stop_order(market, side, size, price, stop_price)
