import kucoin

from kucoin_operations.operation_inteface import IOperation


class CreateStopLossOrder(IOperation):
    def validate(self, **kwargs):
        market = kwargs.get('market')
        side = kwargs.get('side')
        price = kwargs.get('price')
        size = kwargs.get('size')
        stop_price = kwargs.get('stop_price')
        if any(map(lambda x: x is None, [market, side, price, size, stop_price])):
            raise ValueError("Missing argument")
        return True

    def execute(self, kucoin_client: kucoin.client.Market, trade_client: kucoin.client.Trade, **kwargs):
        if self.validate(**kwargs):
            market = kwargs.get('market')
            side = kwargs.get('side')
            price = kwargs.get('price')
            size = kwargs.get('size')
            stop_price = kwargs.get('stop_price')
            return trade_client.create_limit_stop_order(
                symbol=market,
                side=side,
                size=size,
                price=price,
                stopPrice=stop_price
            )
