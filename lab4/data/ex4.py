import datetime
from datetime import datetime, time, timedelta, date

t = datetime.now()
dt2 = datetime.today() - timedelta(4)
difference = abs((t - dt2).total_seconds())

print(difference)