import random

names = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


a = [name.title() for name in names]

# print(a)


def reverse_name(name):
    first, last = name.split()
    return '{} {}'.format(last, first)


b = [reverse_name(name) for name in names]

# print(b)


def gen_pairs():
    first_names = [name.split()[0].title() for name in names]
    while True:
        first, second = None, None
        # while True:
        while first == second:
            first, second = random.sample(first_names, 2)
        yield '{} teams up with {}'.format(first, second)


pairs = gen_pairs()

# for x in range(10):
#     print(next(pairs))


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    names_deduped = []
    for name in names:
        if name not in names_deduped:
            names_deduped.append(name)
    return names_deduped


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    names = sorted(names, key=lambda x: x.split()[1])
    return names


g = sort_by_surname_desc(names)

print(g)
