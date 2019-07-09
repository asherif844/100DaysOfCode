# identify prime numbers only
from collections import Counter, defaultdict
from typing import List, Tuple

prime_numbers = {}
# prime_numbers = []

def retrieve_blocks(number: int) -> List[int]:
    
    list_number = []
    for i in range(2,number):

        list_number.append(i)
    return list_number

top_100 = retrieve_blocks(100)




pairs = {(x, y) for x in range(10) for y in range(x)}
pairs


assert 1+1 ==2, '1+1 = 2 but it didnt'

def smallest_item(xs):
    assert xs, "empty list has no smallest item"
    return min(xs)

# assert smallest_item()

