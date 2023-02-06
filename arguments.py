def add_arguments(parser):
    # get candle
    parser.add_argument('--get_candle', '-g', help='Get candle data', action="store_true")
    # active orders
    parser.add_argument('--get_active_orders', '-ga', help='Get active orders', action="store_true")
    # create stop loss
    parser.add_argument('--create_stop_loss_order', '-cs', help='Create stop loss order', action="store_true")
    # cancel stop loss
    parser.add_argument('--cancel_stop_loss_order', '-cc', help='Cancel stop loss order', action="store_true")
    # update stop loss
    parser.add_argument('--update_stop_loss', '-us', help='Update stop loss order', action="store_true")
    # create take profit
    parser.add_argument('--create_take_profit-order', '-ct', help='Create take profit order', action="store_true")
    # update take profit
    parser.add_argument('--update_take_profit', '-ut', help='Update take profit order', action="store_true")
    # remove take profit
    parser.add_argument('--cancel_take_profit', '-rt', help='Remove take profit order', action="store_true")

    # public arguments
    parser.add_argument('--market', '-m', help='Market for kline data')
    parser.add_argument('--time_frame', '-tf', help='Time frame for kline data')
    parser.add_argument('--side', '-s', help='Side for stop loss order')
    parser.add_argument('--size', '-sz', help='Size for stop loss order')
    parser.add_argument('--price', '-p', help='Price for stop loss order')
    parser.add_argument('--stop_price', '-sp', help='Stop price for stop loss order')
    parser.add_argument('--order_id', '-o', help='Order id for stop loss order')
