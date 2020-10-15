import time
import json
import logging
from math import log

from deribit_api import RestClient, requests


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

with open("config.json") as file:
    KEY, SECRET, AMPLITUDE, SYMBOL, URL_TEST = json.load(file).values()

    if URL_TEST:
        URL_TEST = 'https://test.deribit.com'


class Hedge:
    def __init__(self):
        self.client = RestClient(KEY, SECRET, URL_TEST)
        self.gamma_theta = AMPLITUDE / 100
        self.symbol = SYMBOL

    def get_ticker(self, symbol='BTC-PERPETUAL'):
        res = requests.get(f'https://www.deribit.com/api/v2/public/ticker?instrument_name={symbol}').json()
        return res["result"]["last_price"]

    def get_ticker_op(self, symbol='BTC-PERPETUAL'):
        res = requests.get(f'https://www.deribit.com/api/v2/public/ticker?instrument_name={symbol}').json()
        return res

    def get_equity(self, currency='BTC'):
        account_summary = self.client.get_account_summary(currency)
        return account_summary['equity']

    def delta(self, symbol='BTC'):
        return self.client.get_account_summary("BTC")["delta_total"]

    def last_trade(self, symbol='BTC'):
        return self.client.gettradesbycurrency('BTC')['trades'][0]['price']

    def ln_return(self):
        ticker, trade = self.get_ticker(), self.last_trade()
        resp = log(ticker / trade)
        return resp, ticker, trade

    def delta_hedge(self, ln, delta_total):
        if  ln > self.gamma_theta:
            quaty = round(self.get_ticker() * delta_total / 10) * 10
            last_sell = self.client.sell(instrument=self.symbol, amount=quaty, price=0.00001, type='market')
            logging.info(last_sell)

        elif ln < -self.gamma_theta:
            quaty = (round(self.get_ticker() * delta_total / 10) * 10) * -1
            last_buy = self.client.buy(instrument=self.symbol, amount=quaty, price=0.00001, type='market')
            logging.info(last_buy)    

    def info(self, delta_total, ln, ticker, trade):
        logging.info(f'Delta: {delta_total :.4f} - LN: {ln * 100 :.2f}% - Last trade: {trade} - Last ticker: {ticker}')


    def run(self):
        try:
            while True:
                delta_total = self.delta()
                ln, ticker, trade = self.ln_return()
                
                self.info(delta_total, ln, ticker, trade)
                
                self.delta_hedge(ln, delta_total)
                
                time.sleep(5)
            
        except requests.exceptions.ConnectionError as e:
            logging.info(e)
            time.sleep(10)
            self.run()
            

if __name__ == '__main__':
    Hedge = Hedge()
    Hedge.run()
