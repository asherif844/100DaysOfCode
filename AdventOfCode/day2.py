from collections import Counter
from typing import Set, List

with open ('AdventOfCode/data/day02.txt') as f:
    ids = [line.strip() for line in f]
    # print(ids)
    # print(len(ids))


def char_count_value(word: str) -> Set[int]:
    char_counts = Counter(word)
    return set(char_counts.values())

# def char_count_value(word: str):
#     char_counts = Counter(word)
#     return list(char_counts.values())

# assert char_count_value('aaaabcc') == {4,1,2}
# assert char_count_value('aab') == {2,1}

def checksum(ids: List[str]) -> int:

    num_twos = 0
    num_threes = 0
    for box_id in ids:
        ccv = char_count_value(box_id)
        if 2 in ccv:
            num_twos+=1
            print(box_id, ccv, 'two')
        if 3 in ccv:
            num_threes+=1
            print(box_id, ccv, 'three')
    return num_twos * num_threes        

# assert checksum(['abcdef',  #0
#                 'bababc',   #3,2
#                 'abbcde',   #2
#                 'abcccd',   #3
#                 'aabcdd',   #2,2 
#                 'abcdee',   #2, 3x3
#                 'ababab']) == 12

# print(checksum(ids))

# Given a list of IDs, exactly two differ by exactly one character
# find the remaining characters

def characters_in_common(ids: List[str]) -> str:
    leave_one_outs = Counter()

    for box_id in ids:
        for i in range(len(box_id)):
            leave_one_out = tuple(box_id[:i]+'_'+box_id[(i+1):])
            #  print(leave_one_out)
            leave_one_outs[leave_one_out] += 1
        best_string = leave_one_outs.most_common(1)[0][0]
        best_string = "".join([c for c in best_string if c !='_'])
    return(best_string)
    # return "".join(leave_one_outs.most_common(1)[0])

# characters_in_common(ids)

test_ids = [
'abcde',
'fghij',
'klmno',
'pqrst',
'fguij',
'axcye',
'wvxyz']

print(characters_in_common(ids))