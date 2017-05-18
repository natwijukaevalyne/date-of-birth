#NATWIJUKA EVALYNE
#16/U/945
#BELE

import datetime,calendar
current_year = 2017
date = input("Enter your date of birth (1-31)\n")
endings = ["st","nd","rd"] + 17*["th"]+ ["st","nd","rd"] + 7*["th"] + ["st"]
days = ['Monday','Tuesday','Wednesday','Thursday',
        'Friday','Saturday','Sunday']

month = int(input("Enter the month in which you were born (1-12)\n"))
month_names = ['January', 'February', 'March', 'April', 'May',
               'June', 'July', 'August', 'September', 'October',
               'November', 'December']
year = int(input("What's your age?\n"))
E1 = month_names[month-1]
E2 = int(date)
E3 = (current_year-year)
E4 = date+endings[E2-1]
E5 = calendar.weekday(E3,month,E2)
E6 = days[E5]

this = E1+" ", E2, ",", E3
print("You were born on ",E6,E4,E1, "of the year",E3)
