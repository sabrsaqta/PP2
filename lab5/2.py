#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

import re

with open('row.txt', 'r') as text:
    mytext = text.read()

    # pattern = r'.*8(?:4|1).*'
    pattern = r'.*a(?:b{2}|b{3}).*'
    matches = re.findall(pattern, mytext)

    for match in matches:
        print(match)