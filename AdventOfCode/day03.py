import pprint as p
import re
from typing import NamedTuple, Set, Tuple

with open('AdventOfCode/data/day03.txt') as f:
    a = [line for line in f]
    p.pprint(a)

rgx = "#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)"

Coord = Tuple[int,int]

class Rectangle: 
    id: int
    x_lo: int
    y_lo: int
    x_hi: int
    y_hi: int 

    @staticmethod
    def from_claim(claim: str) -> 'Rectangle':
        id, x_lo, y_lo, width, height = [int(x) for x in re.match(rgx, claim.groups())]
        return Rectangle(id, x_lo, y_lo, width+x_lo, height+y_lo)

    def all_squares(self) -> Set[Coord]:
        return {(i,j)
                for 
        }

claim =  "#123 @ 3,2: 5x4"

assert Rectangle.from_claim(claim)
