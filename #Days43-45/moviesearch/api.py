import requests
import collections

Movie = collections.namedtuple('title', 'imdb_score')


def find_movie_by_title(keyword):
    url = f'http://movie_service.talkpython.fm/api/search/{keyword}'
    resp = requests.get(url)
    resp.raise_for_status()
    results = resp.json()
    movies = []
    for r in results.get('hits'):
        movies.append(Movie(**r))
    return movies
