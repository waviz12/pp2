import datetime
from datetime import datetime, time, timedelta, date
x = datetime.today()
t =  datetime.today() - timedelta(5)
print(f"Today: {x.strftime("%x")}")
print(f"5 days before {t.strftime("%x")}")