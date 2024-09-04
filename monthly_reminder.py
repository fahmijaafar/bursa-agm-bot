import requests
from template import monthly_stocks_to_buy
import os

TOKEN = os.environ['TOKEN']
CHAT_ID = os.environ['CHAT_ID']

# Every 1st day of the month, at 7AM
monthly_reminder = monthly_stocks_to_buy()
if monthly_reminder != 0:
    
    # Send the message to Telegram
    send_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {
        "chat_id": CHAT_ID,
        "text": monthly_reminder,
        "parse_mode": "Markdown"
    }
    response = requests.post(send_url, data=params)
    print(response.json())
