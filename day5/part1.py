#!/usr/bin/env python

import string

with open("inputs") as f:
    lines = list(f)

inputs = [x.strip() for x in lines]
formula = inputs[0]

alphabet = string.ascii_lowercase

polymer_units = True
while polymer_units == True:
    polymer_units = False
    for letter in alphabet:
        if str(letter.upper()+letter.lower()) in formula:
            formula = formula.replace(str(letter.upper()+letter.lower()),'')
            polymer_units = True
        if str(letter.lower()+letter.upper()) in formula:
            formula = formula.replace(str(letter.lower()+letter.upper()),'')
            polymer_units = True

print("The length is %s after all polymers in the formula have reacted." % len(formula))
