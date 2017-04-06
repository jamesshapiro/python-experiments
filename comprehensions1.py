#!/usr/bin/python
"""
File: hello.py

[0, 1, 2, 3] -> [1, 3, 5, 7]

[3, 5, 9, 8] -> [True, False, True, False]

range(10) -> [2, 3, 5, 7]

['apple', 'orange', 'pear'] -> ['A', 'O', 'P']

['apple', 'orange', 'pear'] -> ['apple', 'pear']

['apple', 'orange', 'pear'] ->

[('apple', 5), ('orange', 6), ('pear', 4)]
"""
import math
def is_prime(n):
    if n == 2:
        return True
    for i in range(2,int(math.ceil(math.sqrt(n))+1)):
        if n % i == 0:
            return False
    return True

comp1 = [(x*2)+1 for x in range(4)]
comp2 = [x % 3 == 0 for x in [3, 5, 9, 8]]
comp3 = [x for x in range(2,10) if is_prime(x)]

basket = ['apple', 'orange', 'pear']
comp4 = [x[0].upper() for x in basket]
comp5 = [x for x in basket if len(x) < 6]
comp6 = [(x, len(x)) for x in basket]

print(comp1)
print(comp2)
print(comp3)
print(comp4)
print(comp5)
print(comp6)

