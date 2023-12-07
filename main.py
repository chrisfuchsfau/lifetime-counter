#!/usr/bin/env python3

# Script in Python3 to print my current lifetime

# Todos
    # Print numerically efficient remaining lifetime in sec, min, hours, ...
    # Print rotating clock

import datetime as dt
import dateutil.relativedelta as rd
import time

# Inputs
birthday_dt = dt.datetime(1997, 2, 11, 5, 58)
expected_lifetime_float = 79.12323

# Functions


def Datetime_as_float(datetime):
    datetime_float = datetime.year + (datetime.month - 1) / 12 + (datetime.day-1) / 365.25 
    + datetime.hour / (365.25*24) + datetime.hour / (365.25*24*60) + datetime.second / (365.25*24*60**2)
#    print("Datetime:", " "*8 , datetime, "\nDatetime as float:", datetime_float)
    return datetime_float



def Split_float(divident, divisor, factor):
    integer_float, rest = divmod(divident, 1)
    integer_int = int(integer_float)
    rest_refactor = rest * factor
    print("Float: ", divident, " Integer: ", integer_int, " Rest: ", rest)
    return integer_int, rest_refactor



def Countdown(remain_lifetime_static):
    print("Remaining lifetime floating years static:", remain_lifetime_static) 
    rm_lt_sec = round(remain_lifetime_static * 365.25 * 24 * 60**2)
#    print("Remaining lifetime seconds:", rm_lt_sec, "Type", type(rm_lt_sec)) 
    
    while rm_lt_sec:
        rm_lt_sec -= 1
        time.sleep(1)
        print("Remaining lifetime:", rm_lt_sec, "sec", end="\r")
    print("Congratulations you survived the average")



def Spinning_cursor():
  while True:
    for cursor in '\\|/-':
      time.sleep(1)
      print(f"\r{cursor}", end="", flush=True)



# Main

birthday_float = Datetime_as_float(birthday_dt)

today_float = Datetime_as_float(dt.datetime.today())

remain_time_float = birthday_float + expected_lifetime_float - today_float

#years_int, month_float = Split_float(remain_time_float, 1, 12)
#months_int, day_float = Split_float(month_float, 1, 365.25/12)
#days_int, hour_float = Split_float(day_float, 1, 24)
#hours_int, minute_float = Split_float(hour_float, 1, 60)
#minutes_int, second_float = Split_float(minute_float, 1, 60)
#seconds_int, millisecond_float = Split_float(second_float, 1, 1)

#Spinning_cursor()

Countdown(remain_time_float)

