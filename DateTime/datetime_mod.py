from datetime import datetime, timedelta

weekly_offs_days=['0','6']
holiday_lists=['01-04-2020', '15-04-2020']

working_days = []
weekly_offs = []
holidays = []

from_days=datetime.strptime("01-04-2020","%d-%m-%Y").date()
to_days=datetime.strptime("30-04-2020","%d-%m-%Y").date()

flag_holiday=False
while from_days <= to_days:
    my_day=from_days.strftime("%d")
    my_weekday=from_days.strftime("%w")
    
    if my_weekday not in weekly_offs_days:
        flag_holiday=False
        for holiday_list in holiday_lists:
            temp_holiday_list = datetime.strptime(holiday_list,"%d-%m-%Y").date()
            if from_days == temp_holiday_list:
                holidays.append(my_day)
                flag_holiday=True
        if flag_holiday == False:
            working_days.append(my_day)       
    else:
        weekly_offs.append(my_day)
    from_days=from_days+  timedelta(1)
    
print(f'Working Days{working_days} Total No.: {len(working_days)} '  )
print(f'Weekly:{weekly_offs} Total No.: {len(weekly_offs)}' )
print(f'Holidays{holidays}: Total No.: {len(holidays)}')

