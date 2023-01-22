# kucoin-andicator

## Get data in these time frames
* 1d
* 12h
* 8h
* 4h
* 2h
* 1h
* 30m
* 15m
* 5m

## Data of these fields 
* open 
* close
* high
* low
* ma
* ema
* rsi


## Get Active order/amount [token]
## New buy order (limit, market)
## New sell order (limit, market)
## Set Order stop loss (limit, market) 
## remove stop loss(limit, market)
## All spot - Kucoin
## order profit ?
## remove profit ?



# config.yaml file should be like this
```yaml
kucoin:
  api_key: YOUR_API_KEY
  api_secret: YOUR_API_SECRET
  base_url: https://api.kucoin.com/v1
  timeout: 10
```