import pygame
import pdb
from time import sleep
import user
from decimal import Decimal
from binance.client import Client
import os

class Runner:
    def __init__(self):
        self.tracker = []
        self.moving_averages = []
        self.client = Client(user.API_KEY, user.API_SECRET)

    def run_job(self):
        for i in range(0,20000):
            self.data = self.client.get_all_tickers()
            self.result = self.update_tracker(self.get_bitcoin_usd('BTCUSDT'))
            if len(self.moving_averages) > 4:
                self.moving_averages.pop(0)
            self.append_result(str(self.result[0]))
            if len(self.tracker) > 1 and self.tracker[0] > self.tracker[1]:
                self.play_alert()
                print self.result, "ALERT ALERT - SHUTDOWN RIG"
            else:
                print self.result, "OK"
            print(self.moving_averages)
            sleep(5)

    def update_tracker(self, usd_value):
        if len(self.tracker) < 2:
            self.tracker.append(usd_value)
        else:
            self.tracker.pop(0)
            self.tracker.append(usd_value)
        return self.tracker

    def get_bitcoin_usd(self, coin):
        for record in self.data:
            if coin in record['symbol']:
                usd_value = Decimal(record['price'])
                return usd_value

    def play_alert(self):
        pygame.init()
        pygame.mixer.music.load("music.mp3")
        pygame.mixer.music.play()

    def append_result(self, result):
        self.moving_averages.append(result)

Runner().run_job()
# in progress:
# - SMA with custom intervals

# todos:
# - Plotly
# - Test trades
