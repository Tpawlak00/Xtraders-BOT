import os
from dotenv import load_dotenv

# Load environment variables from .env file
print("LOADING ENV VARIABLES...")
load_dotenv("./envs/.env")

DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")
KLINE_ENDPOINT = os.getenv("KLINE_ENDPOINT")
SYMBOL = os.getenv("SYMBOL")
INTERVAL = int(os.getenv("INTERVAL"))
