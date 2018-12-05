#!/usr/bin/env python

import string

with open("inputs") as f:
    lines = list(f)

inputs = [x.strip() for x in lines]
formula = inputs[0]

alphabet = string.ascii_lowercase

def react_polymer(test_formula):
    polymer_units = True
    while polymer_units == True:
        polymer_units = False
        for letter in alphabet:
            if str(letter.upper()+letter.lower()) in test_formula:
                test_formula = test_formula.replace(str(letter.upper()+letter.lower()),'')
                polymer_units = True
            if str(letter.lower()+letter.upper()) in test_formula:
                test_formula = test_formula.replace(str(letter.lower()+letter.upper()),'')
                polymer_units = True

    return test_formula

shortest_formula = len(formula)
for letter in alphabet:
    new_formula = formula.replace(str(letter.upper()),'')
    new_formula = new_formula.replace(str(letter.lower()),'')
    result = react_polymer(new_formula)
    if len(result) < shortest_formula:
        shortest_formula = len(result)

print("The length of the shortest polymer by removing a single type is: %s" % shortest_formula)
