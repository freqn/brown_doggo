import user
import sched, time
import os
from decimal import Decimal
from binance.client import Client
import pdb

class App:
  def __init__(self, market, coin):
    self.market = market
    self.coin = coin
    self.dataset = []

  def auth_client(self):
    self.client = Client(user.API_KEY, user.API_SECRET)

  def _fetch_prices(self):
    self.prices = self.client.get_all_tickers()
    return self.prices

  def store_data(self, price):
    self.dataset.append(price)

  def get_coin_price(self):
    return [Decimal(x['price'])
            for x
            in self._fetch_prices()
            if x['symbol'] == self.market]

  def runner_start(self):
    self.auth_client()
    price = self.get_coin_price()
    self.store_data(price)
    pdb.set_trace()

App("NCASHETH","NCASH").runner_start()


# api_key = user.API_KEY
# api_secret = user.API_SECRET

# client = Client(api_key, api_secret)

# ## get market depth

# ## place a test market buy order, to place an actual order use the create_order

# ## get all symbol prices
# prices = client.get_all_tickers()
# new_prices = [x for x in prices if not (2 == x.get('id'))]

# for i in prices:
#   if i['symbol'] == "ETHUSDT":
#     usd_value = Decimal(i['price'])
#   elif i['symbol'] == "NCASHETH":
#     ncash_price = Decimal(i['price'])

# ncash_usd_value = ncash_price * usd_value
# ncash_total_value = ncash_price * usd_value * Decimal(25613.36)

# print(ncash_usd_value, ncash_total_value)

# s = sched.scheduler(time.time, time.sleep)
# def get_data(sc): 
#   os.system('clear')
#   # os.system('clear')
#   print(ncash_usd_value, ncash_total_value)
#   s.enter(.05, 0, get_data, (sc,))
# s.enter(.05, 0, get_data, (s,))
# s.run()
