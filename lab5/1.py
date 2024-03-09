#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

import re

with open('row.txt', 'r') as text:
    mytext = text.read()
    matches = re.findall(r'.*a+b*.*', mytext)

    for match in matches:
        print(match)