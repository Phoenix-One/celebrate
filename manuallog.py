#!/usr/bin/python3

# Imports basic python function libraries
import time

def celebrate():

    month = time.strftime('%B')
    print(month)

    if month == "January":
        January()
    elif month == "February":
        February()
    elif month == "March":
        March()
    elif month == "April":
        April()
    elif month == "May":
        May()
    elif month == "June":
        June()
    elif month == "July":
        July()
    elif month == "August":
        August()
    elif month == "September":
        September()
    elif month == "October":
        October()
    elif month == "November":
        November()
    elif month == "December":
        December()
    
def January():
     print('January')

def February():
    print('February')

def March():
    print('March')

def April():
    print('April')

def May():
    print('May')

def June():
    print('June')

def July():
    print('July')

def August():
    print('August')

def September():
    print('September')

def October():
    print('October')

def November():
    print('November')

def December():
    print('December')
