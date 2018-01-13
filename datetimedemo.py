from datetime import datetime
from datetime import timedelta

cday = datetime.strptime('2017-10-27 10:48:22',"%Y-%m-%d %H:%M:%S")
ccday = cday - timedelta(seconds=20)
sday= cday.strftime("%Y-%m-%d %H:%M:%S")
print(ccday)