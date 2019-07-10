test_case = 'dabAcCaCBAcCcaDA'
reducted_test_case = 'dabCBAcaDA'

def same_type(s1: str, s2: str) -> bool:
    return s1.lower() == s2.lower()



def reduct(polymer: str) -> str:
    did_reduce = True
    while did_reduce:
        did_reduce = False
        for i in range(1, len(polymer)):
            unit1 = polymer[i-1]
            unit2 = polymer[i]

            if same_type(unit1, unit2) and unit1 != unit2:
                polymer = polymer[:i-1]+polymer[i+1:]
                did_reduce = True
                # print(polymer)
                break    

    return polymer

reduct(test_case)
# assert reduct(test_case) == reducted_test_case

# with open('AdventOfCode/data/day05.txt') as f:
#     sample = f.read().strip()

# len(reduct(sample))