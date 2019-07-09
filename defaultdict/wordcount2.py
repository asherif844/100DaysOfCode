doc = 'This is going to be an amazing piece of work'

from collections import defaultdict, Counter

c = Counter([0,1,2,0])

word_counts = Counter(doc)

for top_word, top_count in word_counts.most_common(2):
    print(top_word, top_count)

((top_word, top_count), (next_top_word, next_top_count)) = word_counts.most_common(2)

