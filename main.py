import time
from configs import config
from bot.discord_bot import send_message
from bot.kline_fetcher import KlineFetcher
from bot.rsi_calculator import RSICalculator

if __name__ == "__main__":
    print("STARTING BOT...")
    while True:
        # Collect data with kline_fetcher
        fetcher = KlineFetcher()
        rsi_calculator = RSICalculator()
        alert_70 = False
        alert_30 = False

        # Collect data with kline_fetcher
        data = fetcher.fetch_kline_data()
        # calculate RSI
        rsi = rsi_calculator.calculate_rsi(data)
        if rsi > 70 and alert_70 is not True:
            send_message(f"RSI above 70 on {config.SYMBOL}")
            alert_70 = True
        elif rsi < 30 and alert_30 is not True:
            send_message(f"RSI below 30 on {config.SYMBOL}")
            alert_30 = True
        elif 70 > rsi > 30:
            alert_70 = False
            alert_30 = False

        print("RSI:", rsi)
        time.sleep(5)



