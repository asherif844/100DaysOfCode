import re
text = 'Everything is awesome, everything is cool when you are part of the team.  Everything is awesome, when you are living the dream'

# print('Everything is awesome' in text)
# print(text.replace('dream', 'scream'))


text2 = '''
$ python module_index.py |grep ^re
re                 | stdlib | 005, 007, 009, 015, 021, 022, 068, 080, 081, 086, 095
'''

# print(re.findall(r'\d+', text2))

text3 = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been 
the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and 
scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus
PageMaker including versions of Lorem Ipsum"""

# print(text3.split())
# print(re.findall(r'[A-Z][a-z0-9]+', text3))

from collections import Counter

cnt = Counter(re.findall(r'[A-Z][a-z0-9]+', text3))

print(cnt)
