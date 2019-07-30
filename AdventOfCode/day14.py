from typing import List

def digits(x: int) -> List[int]:
    return [int(d) for d in str(x)]

def new_recipes(recipe1: int, recipe2: int) -> List[int]:
    total = recipe1 + recipe2
    return digits(total)


# general tests
assert digits(1000) == [1,0,0,0]
assert digits(103) == [1,0,3]
assert new_recipes(3,7) == [1,0]

def scoreboard(num_steps: int, recipe1: int = 3, recipe2: int = 7):
    scores = [recipe1, recipe2]
    elf1=0
    elf2=1
    while len(scores)<num_steps:
        scores.extend(new_recipes(scores[elf1], scores[elf2]))
        elf1 = (elf1+ scores[elf1]+1) % len(scores)
        elf2 = (elf2+ scores[elf2]+1) % len(scores)
    return scores

assert scoreboard(20) == [3, 7, 1, 0, 1, 0, 1, 2, 4, 5, 1, 5, 8, 9, 1, 6, 7, 7, 9, 2]

def ten_after(n: int):
    scores = scoreboard(n+10)
    return ''.join(str(i) for i in scores[n:n+10])

print(ten_after(509671))
print(ten_after(509671)[:5])

# print(ten_after(2018)[:5])
# print(ten_after(2018))

