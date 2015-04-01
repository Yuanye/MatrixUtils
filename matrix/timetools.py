# -*- coding: utf-8 -*- 
from datetime import date, datetime, timedelta
from time import time, mktime, timezone

ONE_HOUR_SECOND = 60 * 60
ONE_DAY_MINUTE = 60 * 24
ONE_DAY_SECOND = 60 * 60 * 24
DATE_BEGIN = date(1970, 1, 1)
DATETIME_BEGIN = datetime(1970, 1, 1)

def today_days():
    return int((time() - timezone) // ONE_DAY_SECOND)

def ts_to_days(ts):
    return int((ts - timezone) // ONE_DAY_SECOND)

def days2day(days):
    return timedelta(days) + DATE_BEGIN

def day2days(day):
    return (int(float(day) - timezone) // ONE_DAY_SECOND)

def to_date(d):
    if isinstance(d, datetime):
        return d.date()
    return d

def to_datetime(d):
    if isinstance(d, date):
        return datetime(d.year, d.month, d.day)
    return d

def day_begin_second(dt=None):
    if not dt:
        dt = date.today()
    t = mktime(dt.timetuple())
    return t


def day_end_second(dt=None):
    if not dt:
        dt = datetime.now()
    if isinstance(dt, date):
        dt  =  datetime(dt.year, dt.month, dt.day)
    t = dt.replace(hour=0, minute=0, second=0)
    t = mktime(t.timetuple())
    return t + 86400
    #return day_begin_second(dt) + 86400 # 60 * 60 *24

def month_begin_second(dt=None):
    if not dt:
        dt = date.today()
    t = dt.replace(day=1)
    t = mktime(t.timetuple())
    return t

def month_end_second(dt=None):
    if not dt:
        dt = datetime.now()
    if dt.month < 12:
        t = dt.replace(month=dt.month + 1, day=1, hour=0, minute=0, second=0)
    else:
        t = dt.replace(
            year=dt.year + 1, month=1, day=1, hour=0, minute=0, second=0)
    t -= datetime.timedelta(seconds=1)
    t = mktime(t.timetuple())
    return t

def period_string_to_datetime(dt, period):
    """ 
        now = datetime.now()
        dt = period_string_to_date(now, "21:00")
        print now > dt // False or True
    """
    hour, minute = period.split(":")
    return dt.replace(hour=int(hour), minute=int(minute), second=0)

if __name__ == "__main__":
    pass

