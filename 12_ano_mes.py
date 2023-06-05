"""
Write apython program that prints the calendar for a given month and year
"""
import calendar as cal

y = int(input("enter the year: "))
m = int(input("enter the month: "))

# display the calendar
print(cal.month(y, m))
