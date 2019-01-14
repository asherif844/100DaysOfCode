from collections import Counter
import calendar
import itertools
import random
import re
import string
import requests


def num_gen():
    for i in range(5):
        yield i


gen = num_gen()

print(next(gen))

for i in gen:
    print(i)

for i in gen:
    print(i)
