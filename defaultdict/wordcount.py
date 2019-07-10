doc = 'This is going to be an amazing piece of work'

word_counts = {}

# for word in doc:
#     if word in word_counts:
#         word_counts[word] += 1
#     else:
#         word_counts[word] = 1

for word in doc:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1

