# resources
import pygame
import pdb
from time import sleep
import user
from decimal import Decimal
from binance.client import Client
import os

api_key = user.API_KEY
api_secret = user.API_SECRET
client = Client(api_key, api_secret)
tracker = []

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

for i in range(0,20000):
    data = client.get_all_tickers()
    result = update_tracker(get_bitcoin_usd('BTCUSDT'))
    if len(tracker) > 1 and tracker[0] > tracker[1]:
        play_alert()
        print result, "ALERT ALERT"
    print result, "OK"
    sleep(10)
 
# config

# test = get_bitcoin_usd
# pdb.set_trace()
