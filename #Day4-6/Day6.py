import csv
import random
from collections import Counter, defaultdict, deque, namedtuple
from urllib.request import urlretrieve
import numpy as np

# lst = list(range(1000000))
# deq = deque(range(1000000))

# User = {}

# user = User(name='Bob', role='coder')

# print(user.name, user.role)

movies_data = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
movies_csv = 'movies.csv'

urlretrieve(movies_data, movies_csv)
Movie = namedtuple('Movie', 'title  year score')


def get_movies_by_director(data=movies_csv):
    directors = defaultdict(list)
    with open(data) as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except:
                ValueError
                continue
            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)
    return directors


directors = get_movies_by_director()

print(directors.items)
