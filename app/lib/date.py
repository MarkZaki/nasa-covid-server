from datetime import datetime

def get_todays_date():
    return datetime.today().strftime('%Y-%m-%d')