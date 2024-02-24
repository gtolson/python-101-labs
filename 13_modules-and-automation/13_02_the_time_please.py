# Use a built-in Python module to tell you the current date and time.
# Research online, so you can print it in a readable manner.

from datetime import datetime
from datetime import date

#tdate = date.today()
date_time = datetime.now()

f_date_time = date_time.strftime('%Y/%m/%d - %H:%M:%S')

print(f"{date_time}")
print(f"{f_date_time}")