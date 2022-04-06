import pandas as pd

### Basic functions

def reading_wages():
    """
    This functions reads a csv file containing 
    a matrix of days and labour hours price
    return: DataFrame

    """
    wages=pd.read_csv("data/wages_db.csv")

    return wages

def reading_input():
    """
    This funtions reads a text file containing working schedelues for one to several 
    employees and returns a list per employee containing his/her working schedule as string

    return: list
    """

    with open('data/input.txt') as f:
        employees = [line.rstrip(';') for line in f]
    return employees




def extract_names(employees):
    """
    This function extract from a working schedule the names of the employees

    return: list
    """

    names=[]
    for employee in employees:
        x = employee.split("=")[0]
        names.append(x)
    return names    

def extract_schedule(employees):
    """
    This function extract exclusively the days and hours worked for every employee 
    without her/his name

    return: list
    """


    schedules=[]
    for schedule in employees:
        x = schedule.split("=")[1]
        
        schedules.append(x)
    return schedules

def extract_schedule_day(schedules):
    """
    This function extracts for every employee the worked days into a list

    return: list
    """
    days=[]
    for schedule in schedules:
        x = schedule.split(",")
        b=[]
        for day in x:
            y = ''.join(filter(str.isalpha, day))
            b.append(y)
        days.append(b)
    return days


def extract_schedule_hours(schedules):
    hours=[]
    for schedule in schedules:
        x = schedule.split(",")
        h=[j[2:13] for j in x]
        
  
        
 
        hours.append(h)
    return hours

def convert_hours_to_range(hours):
    ranges=[]
    for i in hours:
        
        #starting hour
        minutes_hour=[int(j[0:2])*60 for j in i]
        minutes_alone=[int(j[3:5]) for j in i]
        #lower range
        starting_range = [sum(value) for value in zip(minutes_hour, minutes_alone)]
        
        #closing time
        minutes_hour_c=[int(j[6:8])*60 for j in i]
        minutes_alone_c=[int(j[9:12]) for j in i]
        
        #upper range
        closing_range = [sum(value) for value in zip(minutes_hour_c, minutes_alone_c)]
        
        
        range_worked=list(zip(starting_range, closing_range))
        ranges.append(range_worked)
    return ranges

def cost_function(df_cost,range_input):
    total_hours=int((range_input[1]-range_input[0])/60)
    
    cum=range_input[0]
    pay=0
    for i in range(total_hours):
        cum=cum+60
        if cum<=df_cost["Range"][0]:
            
            pay=pay+df_cost[df_cost.columns[1]][0]
        elif cum>df_cost["Range"][0] and cum<=df_cost["Range"][1]:
            
            pay=pay+df_cost[df_cost.columns[1]][1]
        elif cum>df_cost["Range"][1]:
            
            pay=pay+df_cost[df_cost.columns[1]][2]
       
            
    return pay     

def name_to_payroll(names,dict_range,df_cost):
    for name in names:
        data=dict_range[name]
        total_pay=0
        for j,k in data.items():
            df=df_cost[["Range",j]]
            pay_day=cost_function(df,k)
            total_pay=total_pay+pay_day
        print("The amount to pay "+name+" is: "+str(total_pay)+" USD")

def schedule_with_range_name(names,ranges,days):
    payroll={}
    for k in range(len(ranges)):

        res = dict(zip(days[k], ranges[k]))
        payroll[names[k]]=res
    return payroll  