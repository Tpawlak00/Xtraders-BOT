import pandas as pd
from ta.momentum import RSIIndicator
from bot.kline_fetcher import KlineFetcher

class RSICalculator:
    def calculate_rsi(self, kline_data):
        if not kline_data:
            return None

        closing_prices = [float(candle) for candle in kline_data]
        closing_prices_series = pd.Series(closing_prices)

        # Calculate RSI using ta
        rsi_indicator = RSIIndicator(closing_prices_series, window=14)
        rsi = rsi_indicator.rsi()

        return rsi.iloc[-1] if not rsi.empty else None
