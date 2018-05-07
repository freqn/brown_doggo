import user
import sched, time
import os
from decimal import Decimal
from binance.client import Client

class App:
  def __init__(self, market, coin):
    self.market = market
    self.coin = coin
    self.dataset = []

  def authorize_client(self):
    self.client = Client(user.API_KEY, user.API_SECRET)

  def append_data(self, price):
    data = self.dataset
    data.append(price) if len(data) < 5 else data.pop(0)

  def get_price(self):
    return [Decimal(x['price'])
            for x
            in self._fetch_api_data()
            if x['symbol'] == self.market]

  def start(self):
    self.authorize_client()
    price = self.get_price()
    self.append_data(price)

  def _fetch_api_data(self):
    self.prices = self.client.get_all_tickers()
    return self.prices

App("NCASHETH","NCASH").start()


