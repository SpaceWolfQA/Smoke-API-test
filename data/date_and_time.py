import datetime


def get_today_date():
    today = datetime.date.today()
    return today.strftime('%Y-%m-%d')


def get_tomorrow_date():
    today = datetime.date.today()
    tomorrow_date = today + datetime.timedelta(days=1)
    return tomorrow_date.strftime('%Y-%m-%d')


def get_yesterday_date():
    today = datetime.date.today()
    yesterday_date = today - datetime.timedelta(days=1)
    return yesterday_date.strftime('%Y-%m-%d')


def get_start_month():
    today = datetime.date.today()
    start_month = today.strftime('%Y-%m-01')
    return start_month
