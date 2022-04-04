import pandas as pd

### Basic functions

def reading_wages():
    """
    
    """
    wages=pd.read_csv("data/wages_db.csv")

    return wages

def reading_input():
    """
    """
    #lines=[]
    #with open('data/input.txt') as f:
    #    lines = f.readlines()
    with open('input.txt') as f:
        lines = [line.rstrip(';') for line in f]
    return lines




def extract_names(employees):
    names=[]
    for employee in employees:
        x = employee.split("=")[0]
        names.append(x)
    return names    

def extract_schedule(employees):
    schedules=[]
    for schedule in employees:
        x = schedule.split("=")[1]
        #x = employee.split("=")[1]
        schedules.append(x)
    return schedules

def extract_schedule_day(schedules):
    days=[]
    for schedule in schedules:
        x = schedule.split(",")
        b=[]
        for day in x:
            y = ''.join(filter(str.isalpha, day))
            b.append(y)
        days.append(b)
    return days

