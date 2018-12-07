#!/usr/bin/env python

from numpy import *
import string

with open("inputs") as f:
    lines = list(f)

file = open("coord_map.txt","w")

inputs = [x.strip() for x in lines]

labels = ''.join(sorted(string.ascii_uppercase+string.ascii_lowercase))

def run_calculations(grid_width,grid_height,offset=0):
    # "label" all coords with [A-Za-z]
    coords = {}
    for i in range(0,len(inputs)):
        x,y = inputs[i].split(", ")
        if int(x) > grid_width:
            grid_width = int(x)+offset
        if int(y) > grid_height:
            grid_height = int(y)+offset
        coords[labels[i]] = [int(x)+offset,int(y)+offset]

    # create grid with obtained dimensions
    print("Generating grid...")
    grid = [[' ' for x in range(grid_width)] for y in range(grid_height)]

    print("Calculating distances...")
    for row in range(0,grid_height):
        #print("Processing row %s" % row)
        for col in range(0,grid_width):
            closest_distance = 10000
            for coord in coords:
                x,y = coords[coord]
                distance = abs(int(x) - int(col)) + abs(int(y) - int(row))
                if distance <= closest_distance:
                    if distance == closest_distance:
                        grid[int(row)][int(col)] = "."
                    else:
                        grid[int(row)][int(col)] = coord
                        closest_distance = distance
    for row in grid:
        file.write(''.join(row)+"\n")
    file.write("\n\n")
    return grid

def process_counts(complete_grid):
    print("Counting coords...")
    letter_counts = {}
    for letter in labels:
        letter_counts[letter] = 0
    for row in complete_grid:
        for col in row:
            if col != ".":
                letter_counts[col] += 1
    return letter_counts

compare_results = {}
results_small = run_calculations(200,200,1)
results_large = run_calculations(400,400,1)

processed_grid_small = process_counts(results_small)
processed_grid_large = process_counts(results_large)

for letter in processed_grid_large:
    compare_results[letter] = processed_grid_large[letter]

results_small = run_calculations(200,200,100)
results_large = run_calculations(600,600,100)

processed_grid_small = process_counts(results_small)
processed_grid_large = process_counts(results_large)

for letter in processed_grid_large:
    if compare_results[letter] == processed_grid_large[letter]:
        compare_results[letter] = processed_grid_large[letter]
    else:
        compare_results[letter] = 0

largest_finite_area = 0
for letter in compare_results:
    if compare_results[letter] > largest_finite_area:
        largest_finite_area = compare_results[letter]

print("Largest finite area: %s" % largest_finite_area)
