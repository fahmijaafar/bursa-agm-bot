import requests
from template import monthly_stocks_to_buy
import os

TOKEN = os.environ['TOKEN']
CHAT_ID = os.environ['CHAT_ID']

base_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text="

# Every 1st day of the month, at 7AM

monthly_reminder = monthly_stocks_to_buy()
requests.get(base_url+monthly_reminder)