# calculate the number of the days between days
from datetime import date
date1 = (input("enter the first date: "))
date1 = date1.replace(',', '')
yy = date1[0:4]
yy = int(yy)
mm = date1[5:7]
mm = int(mm)
dd = date1[-2:]
dd = int(dd)


date2 = (input("enter second date: "))
date2 = date2.replace(',', '')
yy2 = date2[0:4]
yy2 = int(yy2)
mm2 = date2[5:7]
mm2 = int(mm2)
dd2 = date2[-2:]
dd2 = int(dd2)

print(f"year diferent: {yy - yy2}, mounts: {mm - mm2}, days: {dd - dd2}")

# this is using date import
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)

delta = l_date - f_date
print(delta.days)
