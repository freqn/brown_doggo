# resources
import pygame
import pdb
from time import sleep
import user
from decimal import Decimal
from binance.client import Client
import os

# config
tracker = []
client = Client(user.API_KEY, user.API_SECRET)

# actions
def get_market_data():
    return client.get_all_tickers()

def get_bitcoin_usd(coin):
    # pdb.set_trace()
    for record in data:
        if coin in record['symbol']:
            usd_value = Decimal(record['price'])
            return usd_value

def update_tracker(usd_value):
    if len(tracker) < 2:
        tracker.append(usd_value)
    else:
        tracker.pop(0)
        tracker.append(usd_value)
    return tracker

def play_alert():
    pygame.init()
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play()

# pdb.set_trace()
for i in range(0,20000):
    data = client.get_all_tickers()
    result = update_tracker(get_bitcoin_usd('BTCUSDT'))
    if len(tracker) > 1 and tracker[0] > tracker[1]:
        play_alert()
        # os.system("say 'DANGER DANGER STRANGER. HOLD ONTO YOU BALLS!!!'")
        print result, "ALERT ALERT - SHUTDOWN RIG"
    else:
        print result, "OK"
    sleep(30)


# todos:
# - Moving average with custom intervals
# - Plotly
# - Test trades
