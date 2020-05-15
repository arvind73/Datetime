import datetime

print('Year is', datetime.date(2020, 5, 15).isocalendar()[0])
print('Week number is', datetime.date(2020, 5, 15).isocalendar()[1])
print('Month number is', datetime.date(2020, 5, 15).isocalendar()[2])


# isocalendar() method of datetime class returns a tuple with the following elements ISO Year, ISO Week Number, ISO month