def num(data,n):
    return data+n
print(num(20250826,10),6)
import datetime
from datetime import datetime,timedelta
original_date = datetime.now()
print(original_date)
now = original_date + timedelta(weeks=2)
print(now)
start_time = datetime(2025,8,6)
nows = start_time + timedelta(days=2)
print(nows)
now1 = "2025/08/26 102433"
start_now1 = datetime.strptime(now1,"%Y/%m/%d %H%M%S")
print(start_now1)