#!/usr/bin/env python

import json

with open("inputs") as f:
    lines = list(f)

inputs = [x.strip() for x in lines]

def get_matching_boxes(inputs):
    boxes = {}
    for box_id in inputs:
        boxes[box_id] = {}
        for box_id2 in inputs:
            diff = 0
            if len(box_id) == len(box_id2):
                for i in range(0,len(box_id)):
                    if box_id[i]!=box_id2[i]:
                        diff+=1
                if diff == 1:
                    for i in range(0,len(box_id)):
                        if box_id[i]!=box_id2[i]:
                            common_letters = box_id[:i] + box_id[i+1:]
                            return common_letters

print(get_matching_boxes(inputs))
