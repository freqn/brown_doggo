import user
import sched, time
from decimal import Decimal
from binance.client import Client
import pdb

api_key = user.API_KEY
api_secret = user.API_SECRET

client = Client(api_key, api_secret)

## get market depth

## place a test market buy order, to place an actual order use the create_order

## get all symbol prices
prices = client.get_all_tickers()
new_prices = [x for x in prices if not (2 == x.get('id'))]

for i in prices:
  if i['symbol'] == "ETHUSDT":
    usd_value = Decimal(i['price'])
  elif i['symbol'] == "NCASHETH":
    ncash_price = Decimal(i['price'])

ncash_usd_value = ncash_price * usd_value
ncash_total_value = ncash_price * usd_value * Decimal(qty)

qty = ""

print(ncash_usd_value, ncash_total_value)

s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
    print(ncash_usd_value, ncash_total_value)
    s.enter(60, 1, do_something, (sc,))

s.enter(60, 1, do_something, (s,))
s.run()
