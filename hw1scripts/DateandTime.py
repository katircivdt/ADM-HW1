#1-)CALENDAR MODULE
#first i set first weekday as monday
#then callendar function returns the day index
#choose these index from liste
import calendar
s=input().split()
calendar.setfirstweekday(0)
x=calendar.weekday(int(s[2]),int(s[0]),int(s[1]))
liste=['MONDAY','TUESDAY','WEDNESDAY',"THURSDAY","FRIDAY",'SATURDAY',"SUNDAY"]
print(liste[x])


#2-)TIME DELTA
#datetime function has function to convert from sring to datetime object.
#take inputs append them into list
#find the difference between time and print them without any float poit
from datetime import datetime

for i in range(int(input())):
    holder=[]
    holder.append(datetime.timestamp(datetime.strptime(input(),"%a %d %b %Y %H:%M:%S %z")))
    holder.append(datetime.timestamp(datetime.strptime(input(),"%a %d %b %Y %H:%M:%S %z")))
    print("{0:.0f}".format(abs(holder[1]-holder[0])))
