from collections import Counter
import calendar
import itertools
import random
import re
import string
import requests


first_half_aphabet = list(string.ascii_lowercase)[:13]

# print(first_half_aphabet)


names = ['ahmed', 'ameena', 'safiya', 'hamza', 'layla']
new_names = []
for name in names:
    if name[0] in first_half_aphabet:
        new_names.append(name.title())

# print(new_names)

new_names_2 = [name.title() for name in names if name[0] in first_half_aphabet]

# print(new_names_2)
resp = requests.get('http://projects.bobbelderbos.com/pcc/harry.txt')
words = resp.text.lower().split()

# print(words[5:15])
cnt = Counter(words)
print(cnt.most_common(5))
print('horror' in words)
