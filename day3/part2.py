#!/usr/bin/env python

from numpy import *
import json
import re

with open("inputs") as f:
    lines = list(f)

inputs = [x.strip() for x in lines]

w, h = 1000,1000;
claim_matrix = [[0 for x in range(w)] for y in range(h)]

for claim in inputs:
    claim_id = re.findall(r'#(\d+) @ \d+,\d+:',claim)
    claim_col = re.findall(r'@ (\d+),\d+:',claim)
    claim_row = re.findall(r'@ \d+,(\d+):',claim)
    claim_width = re.findall(r'@ \d+,\d+: (\d+)x\d+',claim)
    claim_height = re.findall(r'@ \d+,\d+: \d+x(\d+)',claim)

    for i in range(int(claim_col[0]),int(claim_col[0])+int(claim_width[0])):
        for j in range(int(claim_row[0]),int(claim_row[0])+int(claim_height[0])):
            claim_matrix[i][j]+=1

overlaps = {}
for claim in inputs:
    claim_id = re.findall(r'#(\d+) @ \d+,\d+:',claim)
    claim_col = re.findall(r'@ (\d+),\d+:',claim)
    claim_row = re.findall(r'@ \d+,(\d+):',claim)
    claim_width = re.findall(r'@ \d+,\d+: (\d+)x\d+',claim)
    claim_height = re.findall(r'@ \d+,\d+: \d+x(\d+)',claim)

    overlaps[claim_id[0]] = False

    for i in range(int(claim_col[0]),int(claim_col[0])+int(claim_width[0])):
        for j in range(int(claim_row[0]),int(claim_row[0])+int(claim_height[0])):
            if claim_matrix[i][j] > 1:
                overlaps[claim_id[0]] = True

for claim in overlaps:
    if overlaps[claim] == False:
        print(claim)
