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

  def store_data(self, price):
    self.dataset.append(price)

  def get_price(self):
    return [Decimal(x['price'])
            for x
            in self._fetch_api_data()
            if x['symbol'] == self.market]

  def start(self):
    self.auth_client()
    price = self.get_price()
    self.store_data(price)
    pdb.set_trace()

  def _fetch_api_data(self):
    self.prices = self.client.get_all_tickers()
    return self.prices

App("NCASHETH","NCASH").start()


