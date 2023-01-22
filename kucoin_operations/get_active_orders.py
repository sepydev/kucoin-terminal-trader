import kucoin

from kucoin_operations.operation_inteface import IOperation


class GetActiveOrders(IOperation):
    def validate(self, **kwargs):
        return True

    def execute(self, kucoin_client: kucoin.client.Market, trade_client: kucoin.client.Trade, **kwargs):
        if self.validate(**kwargs):
            return kucoin_client.get_active_orders()
