with open('AdventOfCode/data/day01a.txt') as f:
    numbers = [int(line.strip()) for line in f]


def all_frequencies(numbers, start = 0):
    frequency = start

    while True:
        for number in numbers:
            yield frequency
            frequency +=  number

print(all_frequencies(numbers))