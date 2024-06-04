from bs4 import BeautifulSoup
from datetime import datetime
from github import Github
import requests
import os

body = "stocks = ["
now = datetime.now()
year = now.year -1
isaham_url = requests.get('https://www.isaham.my/screener/upcoming-agm')
soup = BeautifulSoup(isaham_url.text, "html.parser")

stock_data = soup.findAll("td")
max_elements_per_line = 11

# Track the current element index
current_index = 0
all_stock = []

while current_index < len(stock_data):
  # Create an empty list to store elements for the current line
  line_elements = []
  
  # Loop until we reach the max elements or the end of data
  for _ in range(max_elements_per_line):
    if current_index >= len(stock_data):
      break
    # Extract text and add to the line
    line_elements.append(stock_data[current_index].text.strip())
    current_index += 1
  all_stock.append(line_elements)

filtered = []
for item in all_stock:
    # filter 1, remove NS
    if '[NS]' not in item[0]:
        # filter 2, stock with gift last year
        if str(year) in item[2]:
            # filter 3, online meeting only
            if 'Online' in item[9]:
              # print(item)
              obj = {
                "stock_name":item[0],
                "stock_price":item[1],
                "stock_gift":item[2],
                "stock_ldtb":item[4],
                "stock_meetingdt":item[6],
                "stock_meetingsite":item[8]
              }
              filtered.append(obj)

body += str(filtered) + "]"

# update GitHub with new Stock data

# login to GitHub
g = Github(os.environ['TOKEN_GITHUB'])
g.get_user().login
repo = g.get_repo("fahmijaafar/bursa-agm-bot")

# update file with latest stock data
file = repo.get_contents("stocks_data_template.py", ref="main")
filePath = file.path
repo.update_file(filePath, "Stock Data updated on " + now.strftime("%d/%m/%Y %H:%M:%S"), body, file.sha, branch="main")
print("File updated!")