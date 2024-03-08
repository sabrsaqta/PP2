#Write a Python program to subtract five days from current date.
import datetime

current_date = datetime.datetime.now()
new_date = current_date - datetime.timedelta(days=5)
print(current_date)
print(new_date)