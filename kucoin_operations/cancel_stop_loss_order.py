import kucoin

from kucoin_operations.operation_inteface import IOperation


class CancelStopLossOrder(IOperation):
    def validate(self, **kwargs):
        order_id = kwargs.get('order_id')
        if any(map(lambda x: x is None, [order_id])):
            raise ValueError("Missing argument")
        return True

    def execute(self, kucoin_client: kucoin.client.Market, trade_client: kucoin.client.Trade, **kwargs):
        if self.validate(**kwargs):
            order_id = kwargs.get('order_id')
            return trade_client.cancel_client_stop_order(order_id)
