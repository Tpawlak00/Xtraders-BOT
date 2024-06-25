import requests
from configs import config

def send_message(message):
    data = {'content': message}
    requests.post(config.DISCORD_WEBHOOK, json=data)
