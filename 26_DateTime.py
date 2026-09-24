from datetime import date
# my_date=date(2000,12,18)
today=date.today()
print(today)

print("Year: ",today.year)
print("month: ",today.month)
print("day: ",today.day)
#---------------------------------

from datetime import time
t=time(16,29,10,5)
print(t)
print("hours: ",t.hour)
print("minutes: ",t.minute)
print("seconds: ",t.second)
print("microseconds: ",t.microsecond)

#-------------------------------------

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
#To retrieve the formatted string
print(now.strftime("%d-%m-%y"))
print(now.strftime("%d-%B-%y")) #24-September-26
print(now.strftime("%A-%m-%y")) #Thursday-09-26


from datetime import datetime
value=input("Enter date in DD-MM-YYYY Format ")
d=datetime.strptime(value,"%d-%m-%Y")
print(d.strftime("%A-%B-%Y"))