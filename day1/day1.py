#!/usr/bin/env python

with open("inputs") as f:
    lines = list(f)

frequency = 0
inputs = [x.strip() for x in lines]
for freq in inputs:
    if freq[0] == '-':
        frequency-=int(freq[1:])
    elif freq[0] == '+':
        frequency+=int(freq[1:])

print(frequency)
