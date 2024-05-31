import datetime
from datetime import datetime
from stocks_data import stocks
month_name = datetime.now().strftime("%B")
day = datetime.now().day
year = datetime.now().year

# to be called once a month(preferably 1st day of the month)
def monthly_stocks_to_buy():
    
    stocks_this_month = []
    for stock in stocks:
        if month_name.upper() in stock['stock_ldtb']:
            stock_str = stock['stock_name'] + " - " + stock['stock_price'] + " - " + stock['stock_gift'] + " - " + stock['stock_ldtb']
            stocks_this_month.append(stock_str)

    monthly_reminder_stocks = f"""The following are stocks that provide good rewards which you should buy in {month_name} {year}\n
    Name | Price | Last Gift | Last Day to Buy
    """

    if len(stocks_this_month)>0:
        for stock in stocks_this_month:
            monthly_reminder_stocks += stock + "\n"

        return monthly_reminder_stocks
    else:
        return "There are no good stocks to buy for the AGM/EGM gifts this month! Time for a good rest from all those stressful meetings :D"

# to be called daily, for a stock which the last date to buy is today(8AM every morning?)
def daily_stocks_to_buy():
    
    stocks_today = []
    today = str(day) + " " + month_name.upper()
    for stock in stocks:
        if today in stock['stock_ldtb']:
            stock_str = stock['stock_name'] + " - " + stock['stock_price'] + " - " + stock['stock_gift'] + " - " + stock['stock_meetingsite']
            stocks_today.append(stock_str)

    daily_reminder_stocks = f"""Today is your last chance to buy the following stocks for AGM/EGM gifts! Dont forget to register for the event if you've already bought the stocks.\n
    Name | Price | Last Gift | Register Link
    """
    if len(stocks_today) > 0:
        for stock in stocks_today:
            daily_reminder_stocks += stock + "\n"
    
        return(daily_reminder_stocks)
    else:
        return 0
    
# to be called daily, for stocks that the meeting is today (called at 7AM)
def daily_stocks_meeting():
    
    stocks_today = []
    today = str(day) + " " + month_name.upper()
    for stock in stocks:
        if today in stock['stock_meetingdt']:
            stock_str = stock['stock_name'] + " - " + stock['stock_gift'] + " - " + stock['stock_meetingsite']
            stocks_today.append(stock_str)

    daily_reminder_stocks_meeting = f"""Today is the AGM/EGM date for the following stock(s). Kindly prepare your suits and get online!\n
    Name | Last Gift | Meeting Site
    """
    if len(stocks_today) > 0:
        for stock in stocks_today:
            daily_reminder_stocks_meeting += stock + "\n"
    
        return(daily_reminder_stocks_meeting)
    else:
        return 0