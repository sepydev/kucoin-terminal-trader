# kucoin-terminal-trader








# config.yaml file should be like this
```yaml
kucoin:
  api_key: YOUR_API_KEY
  api_secret: YOUR_API_SECRET
  api_passphrase : <api_passphrase>
  base_url: https://api.kucoin.com
  timeout: 10
```


# config.yaml file should be like this (sandbox)
```yaml
kucoin:
  api_key: api_key
  api_secret: YOUR_API_SECRET
  api_passphrase : <api_passphrase>
  base_url: https://openapi-sandbox.kucoin.com
  timeout: 10
```


# To get candle use this command 

#### time frames:
* 1day
* 12hour
* 8hour
* 4hour
* 2hour
* 1hour
* 30min
* 15min
* 5min
```commandline
python3 main.py --get_candle --market BTC-USDT --time_frame 1min
```
#### Output columns is: 
* open 
* close
* high
* low
* ma
* ema
* rsi


# To get all active orders
```commandline
python3 main.py --get_active_orders
```

# To create stop loss order 

```commandline
python3 main.py --create_stop_loss_order --market BTC-USDT --side sell --price 0.01 --size 0.0001 --stop_price 0.001

```


# To cancel stop loss order 
```commandline
python3 main.py --cancel_stop_loss_order --order_id vs8ueov0tfb3dkgv000v3lee
```




