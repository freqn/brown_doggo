from binance.client import Client
import pdb

from token import API_KEY, API_SECRET

client = Client(API_KEY, API_SECRET)

# get market depth
depth = client.get_order_book(symbol='BNBBTC')

# place a test market buy order, to place an actual order use the create_order function

# get all symbol prices
prices = client.get_all_tickers()

for i in prices:
    print(i)
