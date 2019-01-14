import csv
import random
from collections import Counter, defaultdict, deque, namedtuple
from urllib.request import urlretrieve
import numpy as np


words = """ 

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

""".split()


common_words = {}

for word in words:
    if word not in common_words:
        common_words[word] = 0

    else:
        common_words[word] += 1


# print(common_words.items())
for k, v in sorted(common_words.items(), key=lambda x: x[1], reverse=True):
    print(k, v)
