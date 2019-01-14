from datetime import datetime
from datetime import timedelta 

t = timedelta(days = 4, hours = 10)

# print(t.seconds/3600)

eta = timedelta(hours =6)

today = datetime.today()

print((today+eta))