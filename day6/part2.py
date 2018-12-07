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
    region_count = 0
    for row in range(0,grid_height):
        #print("Processing row %s" % row)
        for col in range(0,grid_width):
            total_distance = 0
            for coord in coords:
                x,y = coords[coord]
                total_distance += abs(int(x) - int(col)) + abs(int(y) - int(row))
            if total_distance < 10000:
                region_count += 1
                #print("Total distance from (%s,%s): %s" % (col,row,total_distance))

    return region_count

region_count = run_calculations(600,600,100)
print("Region size containing locations < 10000 to all points: %s" % region_count)
