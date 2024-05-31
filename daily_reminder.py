import requests
from template import daily_stocks_meeting, daily_stocks_to_buy
import os
import datetime

TOKEN = os.environ['TOKEN']
BOT_USERNAME = os.environ['BOT_USERNAME']
CHAT_ID = os.environ['CHAT_ID']

base_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text="


now = datetime.datetime.now()
print(now.hour)

# Every day, at 7AM
if now.hour == 7:
    daily_reminder_1 = daily_stocks_to_buy()
    if daily_reminder_1 != 0:
        requests.get(base_url+daily_reminder_1)

# Every day, at 8AM
if now.hour == 8:
    daily_reminder_2 = daily_stocks_meeting()
    if daily_reminder_2 != 0:
        requests.get(base_url+daily_reminder_2)