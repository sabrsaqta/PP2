#Write a Python program to drop microseconds from datetime.

import datetime

current_date = datetime.datetime.now()
new_date = current_date.replace(microsecond=0)
print(current_date)
print(new_date)