from typing import Iterator, List, Set

with open('AdventOfCode/data/day01a.txt') as f:
    numbers = [int(line.strip()) for line in f]
    
print(sum(numbers))
print(len(numbers))


def all_frequencies(numbers: List[int], start: int = 0)-> Iterator[int]:
    """
    generate all frequencies
    by adding the numbers in a cycle
    and we need to start at 0
    """
    
    frequency = start

    while True:
        for number in numbers:
            yield frequency
            frequency +=  number

def first_repeat_frequency(numbers: List[int], start: int = 0) -> int:
    seen = set()
    for frequency in all_frequencies(numbers, start):
        if frequency in seen:
            return frequency
        else:
            seen.add(frequency)

assert first_repeat_frequency([1,-1])==0
assert first_repeat_frequency([+7, +7, -2, -7, -4]) == 14

print(first_repeat_frequency(numbers))
