import re
from collections import Counter

movies = '''1. Citizen Kane (1941)
2. The Godfather (1972)
3. Casablanca (1942)
4. Raging Bull (1980)
5. Singin' in the Rain (1952)
6. Gone with the Wind (1939)
7. Lawrence of Arabia (1962)
8. Schindler's List (1993)
9. Vertigo (1958)
10. The Wizard of Oz (1939)'''
movies_list = movies.split('\n')
# print(movies_list)

for i in movies_list:
    if len(re.findall('\w+', i))-1 == 2:
        print(i)
