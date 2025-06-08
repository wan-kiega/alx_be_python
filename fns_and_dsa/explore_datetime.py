import datetime
from datetime import date, timedelta
def get_current_datetime():
    current_date = datetime.datetime.now()
    format_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(format_date)

get_current_datetime()

def calculate_future_date():
    number_days = int(input("Enter the number of days: "))
    today = date.today()
    future_date = today + timedelta(days = number_days)
    print(future_date)

calculate_future_date()
