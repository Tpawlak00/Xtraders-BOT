# Discord RSI Bot

This is a Discord bot that fetches spot K-line data for the SOL/USDT pair from Bybit, calculates the RSI (Relative Strength Index) for this symbol based on the closing price, and sends a message to a Discord channel if the RSI value is over 70 or below 30. The bot uses the 1H (1 hour) time frame.

You can either create your own server and change webhook address in .env or just join to this server https://discord.gg/2uqcXGhrCd
## Requirements

- requests~=2.32.3
- pybit~=5.7.0
- pandas~=2.2.2
- ta~=0.11.0
- python-dotenv~=1.0.1

## Setup

1. **Clone the repository**

   ```sh
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo

2. **Create a .env file or use one that is already created**

Create a .env file in the root directory of the project and add your Discord webhook:

- **DISCORD_WEBHOOK = https://discord.com/api/webhooks/1254832911526527078/cx0MyyULVw6Le4XHEK0a8ewCIcoCacVExg71gZ57DRAPft7b-mmDOkOYvxo-U1-Nac0J**
- KLINE_ENDPOINT = "https://api.bybit.com/v2/public/kline/list"
- SYMBOL = SOLUSDT
- INTERVAL = 60

3. **Configuring dockerfile or use the one that is already created**

To properly create docker container change the following enviroment variables and add your Discord webhook:

- ENV DISCORD_WEBHOOK = https://discord.com/api/webhooks/1254832911526527078/cx0MyyULVw6Le4XHEK0a8ewCIcoCacVExg71gZ57DRAPft7b-mmDOkOYvxo-U1-Nac0J
- ENV KLINE_ENDPOINT = "https://api.bybit.com/v2/public/kline/list"
- ENV SYMBOL = SOLUSDT
- ENV INTERVAL = 60

4. **Creating docker container**
To create docker container, run this command

   docker build -t discord-rsi-bot .
5. **Running BOT with docker**

After properly creating container, run command:

    docker run --env-file ./envs/.env discord-rsi-bot

This will run BOT. 


