import datetime


def last_of_date(str_date):    
    yy = int(str_date[0:4])
    mm = int(str_date[5:7])
    dd = int(str_date[8:10])
    day_str = datetime.date(yy, mm, dd) - datetime.timedelta(1)
    last_day = day_str.strftime('%Y-%m-%d')
    return last_day


def datetime_to_string(d):
    if isinstance(d, datetime.datetime):
        return d.__str__()
