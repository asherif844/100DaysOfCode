from datetime import datetime
from datetime import date 

today = datetime.today()

todayDate = date.today()

# print(todayDate.year)

christmas = date(2018,12,25)
# print((christmas-todayDate).days)

if christmas is not todayDate:
    print('Sorry there are still {} days left before Christmas'.format((christmas - todayDate).days))
else:
    print('Merry Christmas')