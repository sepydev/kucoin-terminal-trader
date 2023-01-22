import kucoin

from kucoin_operations.operation_inteface import IOperation


class UpdateTakeProfit(IOperation):
    def validate(self, **kwargs):
        order_id = kwargs.get('order_id')
        stop_price = kwargs.get('stop_price')
        if any(map(lambda x: x is not None, [order_id, stop_price])):
            raise ValueError("Missing argument")
        return True

    def execute(self, kucoin_client: kucoin.client.Market, trade_client: kucoin.client.Trade, **kwargs):
        if self.validate(**kwargs):
            order_id = kwargs.get('order_id')
            stop_price = kwargs.get('stop_price')
            return kucoin_client.update_take_profit_order(order_id, stop_price)
