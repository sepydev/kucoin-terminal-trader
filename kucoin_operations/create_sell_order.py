import kucoin

from kucoin_operations.operation_inteface import IOperation


class CreateSellOrder(IOperation):
    def validate(self, **kwargs):
        market = kwargs.get('market')
        limit = kwargs.get('limit')
        price = kwargs.get('price')
        size = kwargs.get('size')
        if any(map(lambda x: x is not None, [market, limit, price, size])):
            raise ValueError("Missing argument")
        return True

    def execute(self, kucoin_client: kucoin.client.Market, trade_client: kucoin.client.Trade, **kwargs):
        if self.validate(**kwargs):
            market = kwargs.get('market')
            limit = kwargs.get('limit')
            price = kwargs.get('price')
            size = kwargs.get('size')
            return kucoin_client.create_sell_order(market, size, price, limit)
