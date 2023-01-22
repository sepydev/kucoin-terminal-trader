import argparse

from kucoin.client import Market
from kucoin.client import Trade

import yaml

from arguments import add_arguments
from kucoin_operations.cancel_stop_loss_order import CancelStopLossOrder
from kucoin_operations.cancel_take_profit import CancelTakeProfit
from kucoin_operations.create_buy_order import CreateBuyOrder
from kucoin_operations.create_sell_order import CreateSellOrder
from kucoin_operations.create_stop_loss_order import CreateStopLossOrder
from kucoin_operations.create_take_profit_order import CreateTakeProfitOrder
from kucoin_operations.get_active_orders import GetActiveOrders
from kucoin_operations.get_candle import GetCandle
from kucoin_operations.update_stop_loss import UpdateStopLoss
from kucoin_operations.update_take_profit import UpdateTakeProfit


def get_operation(args: argparse.Namespace) -> str:
    for key, value in args.__dict__.items():
        if isinstance(value, bool):
            return key


parser = argparse.ArgumentParser(description='Kucoin trading operations')
add_arguments(parser)
args = parser.parse_args()

response = None

operations = {
    'get_candle': GetCandle,
    'get_active_orders': GetActiveOrders,
    'create_stop_loss_order': CreateStopLossOrder,
    'create_buy_order': CreateBuyOrder,
    'cancel_stop_loss_order': CancelStopLossOrder,
    'create_sell_order': CreateSellOrder,
    'update_stop_loss': UpdateStopLoss,
    'create_take_profit_order': CreateTakeProfitOrder,
    'update_take_profit': UpdateTakeProfit,
    'cancel_take_profit': CancelTakeProfit,

}

with open("config.yaml") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

api_key = config['kucoin']['api_key']
api_secret = config['kucoin']['api_secret']
base_url = config['kucoin']['base_url']
kucoin_client = Market(url=base_url)

trade_client = Trade(key='', secret='', passphrase='', is_sandbox=False, url='')

operation_class = operations.get(get_operation(args))
if operation_class:
    operation_obj = operation_class()
    response = operation_obj.execute(kucoin_client, trade_client, **args.__dict__)
    print(response)
else:
    print(f"Invalid operation: {get_operation(args)}")
