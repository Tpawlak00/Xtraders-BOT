import requests
import time
from configs import config
from pybit.unified_trading import HTTP
from datetime import datetime, timedelta


class KlineFetcher:
    BYBIT_KLINE_ENDPOINT = config.KLINE_ENDPOINT
    session = HTTP(testnet=True)

    def fetch_kline_data(self, symbol=config.SYMBOL, interval=config.INTERVAL):
        now = datetime.now()
        data = self.session.get_kline(
                    category="linear",
                    symbol=symbol,
                    interval=interval,
                    start=datetime.timestamp(now - timedelta(hours=14)),
                    end=datetime.timestamp(now),
                )
        close_prices = []
        for row in data['result']['list']:
            close_prices.append(row[4])

        return close_prices
