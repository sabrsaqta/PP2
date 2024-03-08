#Write a Python program to calculate two date difference in seconds.

import datetime

l1 = []
l2 = []
y1, m1, d1 = int(input('Year_1: ')), int(input('Month_1: ')), int(input('Day_1: '))
y2, m2, d2 = int(input('Year_2: ')), int(input('Month_2: ')), int(input('Day_2: '))

difference = datetime.datetime(y1, m1, d1) - datetime.datetime(y2, m2, d2)
difference_in_seconds = difference.total_seconds()
print(abs(difference_in_seconds))
