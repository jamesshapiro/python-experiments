#!/usr/bin/env python3

"""
File: dict-key.py

Experiment to remind myself that Python uses "==" rather than "is"
when comparing keys in a dictionary.

Output:
first_cat == second_cat? True!
first_cat is second_cat? False!
American Shorthair
zero point zero
"""

dict = {}
first_cat = "cat"
second_cat = "ca"
second_cat = second_cat + "t"
print("first_cat == second_cat: {}".format(first_cat == second_cat))
print("first_cat is second_cat: {}".format(first_cat is second_cat))
dict[first_cat] = "Siamese"
dict[second_cat] = "American Shorthair"
print(dict[first_cat])

dict[0] = 'zero'
dict[0.0] = 'zero point zero'
print(dict[0])

