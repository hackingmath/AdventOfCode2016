# Advent of Code 2016 Day 8
# https://adventofcode.com/2016/day/8

import time
#from random import randint
from itertools import combinations

starting_time = time.time()
testlines = ['rect 3x2','rotate column x=1 by 1','rotate row y=0 by 4']
GRIDW = 50
GRIDH = 6
GRID = []
for i in range(GRIDH):
    GRID.append([])
    for j in range(GRIDW):
        GRID[i].append(0)

with open('day08.txt') as f:
    lst = list()
    lines = f.readlines()
    lines = [x.strip("\n") for x in lines]
    lines = [x.split(' ') for x in lines]
    print(len(lines),lines)

def part1(testing=False):
    global GRID
    for x in lines:
        newGRID = GRID[::]
        print(x)
        if x[0] == 'rect':
            s = x[1] #string like '17x1'
            s = s.split("x") #now it's a list ['17','1']
            #print(s)
            w = int(s[0]) #width of rect
            h = int(s[1]) #height of rect
            print("w,h:",w,h)
            for i in range(h):
                for j in range(w):
                    newGRID[i][j] = 1
        if x[0] == 'rotate':
            if x[1] == 'row':
                row = int(x[2].strip('y='))
                shift = int(x[4])
                newrow = [0]*GRIDW
                for i,cell in enumerate(GRID[row]):
                    newrow[(i+shift)%GRIDW] = cell
                newGRID[row] = newrow[::]
            elif x[1] == 'column':
                col = int(x[2].strip('x='))
                shift = int(x[4])
                newcol = [0]*GRIDH
                oldcol = [GRID[i][col] for i in range(GRIDH)]
                for i,cell in enumerate(oldcol):
                    newcol[(i+shift)%GRIDH] = cell
                for j in range(GRIDH):
                    newGRID[j][col] = newcol[j]
            GRID = newGRID[::]

        for row in GRID:
            print(row)

    ons = 0
    for row in GRID:
        for col in row:
            if col == 1:
                ons += 1
    print("ons:",ons)


def part2():
    pass

part1(True) #105 too low.
#print(part2())
print("Time (secs):",time.time()-starting_time)