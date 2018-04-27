import binance
from setup import API_KEY, API_SECRET
binance.set(API_KEY, API_SECRET)


print binance.prices()
