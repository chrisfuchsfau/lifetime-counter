#!/usr/bin/env python3

# Script in py to print my current lifetime

# Todos
    # Allow float type years

import datetime as dt
import dateutil.relativedelta as rd
import time

# Inputs
birthday_dt = dt.datetime(1997, 2, 11, 5, 58)
expected_lifetime_years = 79

# Functions

def Calc_lifetime(birth_dt, ex_lt_y):
    ex_death_date = birth_dt + rd.relativedelta(years = ex_lt_y)
    today = dt.datetime.today()
    
    # Calc diff
    rm_lt = today - birth_dt 
    rm_lt_s = round(rm_lt.total_seconds())
    
    # ex_lifetime = dt.timedelta(days=18)
    
    # ex_death_dt = birth_dt + dt.timedelta(ex_lifetime)
    
    
    #print("Birth date:", birth_dt)
    #print("Ex. death date:", ex_death_date)
    #print("Ex. remaining lifetime:", rm_lt_s, "sec")
   
    return rm_lt_s

def Countdown(remaining_lifetime_sec_static):
    
    rm_lt = remaining_lifetime_sec_static
    
    while rm_lt:
        print("Remaining lifetime:", rm_lt, "sec", end="\r")
        time.sleep(1)
        rm_lt -= 1 
    print("Congratulations you survived the average")
    


# Main

remaining_lifetime_sec_static = Calc_lifetime(birthday_dt, expected_lifetime_years)
Countdown(remaining_lifetime_sec_static)

