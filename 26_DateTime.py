from datetime import date
# my_date=date(2000,12,18)
today=date.today()
print(today)

print("Year: ",today.year)
print("month: ",today.month)
print("day: ",today.day)
#---------------------------------
from datetime import datetime
now=datetime.now()
print (now)
print("Year: ",now.year)
print("month: ",now.month)
print("day: ",now.day)
print("hours: ",now.hour)
print("minutes: ",now.minute)
print("seconds: ",now.second)
print("microseconds: ",now.microsecond)

