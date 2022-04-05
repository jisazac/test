### app file

from pip import main
from utils.utils import *

#Read inputs
df_cost=reading_wages()
employees=reading_input()

#Extract information
names=extract_names(employees)
schedules=extract_schedule(employees)
days=extract_schedule_day(schedules)
hours=extract_schedule_hours(schedules)

#Reshape information
range_w=convert_hours_to_range(hours)
m=schedule_with_range_name(names,range_w,days)

#Calculate
final=name_to_payroll(names,m,df_cost)


