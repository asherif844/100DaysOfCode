import json
import requests
from pprint import pprint
url = 'http://www.omdbapi.com/?t=a+few+good+men&y=1992&plot=full'+'&apikey=5b9dde69'
r = requests.get(url)

data = json.loads(r.text)

ratings = []
for item in data['Ratings']:
    if item['Source'] == 'Rotten Tomatoes':
        ratings.append(item)

print(ratings)
