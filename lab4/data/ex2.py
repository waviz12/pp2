import datetime
from datetime import datetime, time, timedelta, date

today = datetime.today()
yesterday = datetime.today() - timedelta(1)
tomorrow = datetime.today() + timedelta(1)
print(f"Yesterday {yesterday.strftime("%x")}, Today : {today.strftime("%x")},  Tomorrow {tomorrow.strftime("%x")}")