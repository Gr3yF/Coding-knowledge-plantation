from datetime import datetime
#from datetime import datetime

print("Create a Datetime object")
#Datetime obejects have attributes representing the year, month, date, hour, second, microsecond, and timezone
#To creat a datetime object, you must provide a min. of the year, month, and date
print("Example 1")
black_monday = datetime(1987, 10, 19)
print(black_monday)
print("Example 2: Datetime from a string")
#Takes two arguments; string to convert and a format string
black_monday_str = "Monday, October 19, 1987. 9:30 am"
format_str = "%A, %B %d, %Y. %I:%M %p"
print(datetime.strptime(black_monday_str, format_str))

#Datetime from string format
#YEAR
# %y Without century (01,02,...,98,99)
# %Y With century (0001,0002,...,1998,1999,...,9999)

# MONTH
# %b Abbreviated names (Jan,Feb,...,Nov,Dec)
# %B Full names (January,February,...November,December)
# %m As numbers (01,02,...,11,12)

# DAY OF MONTH
# %d (01,02,...,30,31)

#WEEKDAY
# %a Abbreviated name (Sun,...Sat)
# %A Full name (Sunday,...Saturday)
# %w Number (0,...,6)

# TIME
# %H 24 hour (00,01,...23)
# %I 12 hour (01,02,...12) 
# %M Minutes (01,02,...,59)
# %S Seconds (00,01,...59)
# %f Mirco-seconds (000000,000001,...999999) 
# %p AM/PM (AM,PM)

#Functions
print("datetime.now() function returns a datetime representing the current time")
print(datetime.now()) #handy for capturing an event when something occured or to check how long a calc. took to run

print("datetime.strftime() function, creates a str from a datetime object and takes a output format string as an argument")
n_dt = datetime(1929, 10, 29)
print(n_dt)
print(type(n_dt))
str_n_dt = n_dt.strftime("%a, %b %d, %Y")
print(str_n_dt)
print(type(str_n_dt))

#Attributes
#year, month, day, hour, minute, second
print(n_dt.year)

#Difference between datetimes
#you can compare using >, <, & ==
#subtracting datetimes outputs a timedelta
s_dt = n_dt - black_monday
print(type(s_dt))

#creating relative datetimes
from datetime import timedelta #can add this to the top import like this 'from datetime import datetime, timedelta'
offset = timedelta(weeks=1)
week_earlier_dt = n_dt - offset
print(n_dt, '\n', week_earlier_dt,'\n', type(week_earlier_dt))