"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

while True:
  prompt = (input("Input the month and year, comma separated: "))
  
  separate_numbers = prompt.split(',')
  print(separate_numbers)
  print(len(separate_numbers))
  new_numbers = []
    
  if(len(separate_numbers) == 1):
    new_numbers.append(int(separate_numbers[0]))
    print(new_numbers)
  elif(len(separate_numbers) == 2):
    for i in separate_numbers:
      j = i.replace(' ', '')
      new_numbers.append(int(j))
      print(new_numbers)
    
  if(len(new_numbers) == 1):
    month = new_numbers[0]
    print(calendar.month(2020, month))
  elif(len(new_numbers) == 2):
    month = new_numbers[0]
    year = new_numbers[1]
    print(calendar.month(year, month))

  
  
  
  
  
  
  
# def display_calendar(month, year):
  
#   m = (input("Input the month and year, comma separated: "))
#   separate_numbers = m.split(',')
#   for i in separate_numbers:
#     j = i.replace(' ', '')
#     new_numbers = []
#     new_numbers.append(int(separate_numbers[0]))
#     new_numbers.append(int(j))
  
#   month = new_numbers[0]
#   year = new_numbers[1]
  
#   if (year):
#     print(calendar.month(year, month))
#   else:
#     print(calendar.month(2020, month))

# display_calendar()