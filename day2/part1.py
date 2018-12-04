#!/usr/bin/env python

import json

with open("inputs") as f:
    lines = list(f)

boxes = {}
inputs = [x.strip() for x in lines]
for box_id in inputs:
    boxes[box_id] = {}
    for letter in box_id:
        boxes[box_id][letter] = 0

for box_id in inputs:
    for letter in box_id:
        boxes[box_id][letter] = box_id.count(letter)

for box_id in inputs:
    boxes[box_id]['two'] = False
    boxes[box_id]['three'] = False
    for letter in box_id:
        if box_id.count(letter) == 2:
            boxes[box_id]['two'] = True
        if box_id.count(letter) == 3:
            boxes[box_id]['three'] = True

count_two=0
count_three=0

for box_id in inputs:
    if boxes[box_id]['two']:
        count_two+=1
    if boxes[box_id]['three']:
        count_three+=1

print(count_two*count_three)
