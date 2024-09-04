import datetime
from prettytable import PrettyTable
from datetime import datetime
from stocks_data import stocks
month_name = datetime.now().strftime("%B")
day = datetime.now().day
year = datetime.now().year

# to be called once a month(preferably 1st day of the month)
def monthly_stocks_to_buy():
    
    # Create a PrettyTable object
    table = PrettyTable()
    table.field_names = ["Name", "Price", "Last Day", "Gift"]

    # Helper function to truncate text if needed
    def truncate(text, length):
        return text if len(text) <= length else text[:length]

    stocks_this_month = []
    if not stocks_this_month:
        return 0
    for stock in stocks:
        if month_name.upper() in stock['stock_ldtb']:
            # Truncate each field to fit within the character limit
            stock_name = stock['stock_name']  # truncated to 6 characters
            stock_price = truncate(stock['stock_price'], 5)
            stock_ldtb = convert_date_format(stock['stock_ldtb'])  # convert date format
            stock_gift = truncate(stock['stock_gift'], 10)  # truncated to 10 characters
            
            table.add_row([stock_name, stock_price, stock_ldtb, stock_gift])

    table_str = table.get_string()
    monthly_reminder_stocks = f"""The following are stocks that provide good rewards which you should buy in {month_name} {year}\n\n```\n{table_str}\n```"""
    
    return monthly_reminder_stocks

# to be called daily, for a stock which the last date to buy is today(8AM every morning?)
def daily_stocks_to_buy():
    
    stocks_today = []
    today = str(day) + " " + month_name.upper() + " " + str(year)
    for stock in stocks:
        if today == stock['stock_ldtb']:
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
    today = str(day) + " " + month_name.upper() + " " + str(year)
    for stock in stocks:
        if today == stock['stock_meetingdt']:
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

#convert long date to short date
def convert_date_format(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%d %B %Y")
        return date_obj.strftime("%d/%m")
    except ValueError:
        return date_str
