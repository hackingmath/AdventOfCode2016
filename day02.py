# Advent of Code 2016 Day 2
# https://adventofcode.com/2016/day/2

import time
#from random import randint
from itertools import combinations

starting_time = time.time()

GRID = [[1,2,3],[4,5,6],[7,8,9]]
GRID2 = [[0,0,1,0,0],[0,2,3,4,0],[5,6,7,8,9],[0,'A','B','C',0],[0,0,'D',0,0]]


with open('day02.txt') as f:
    lst = list()
    lines = f.readlines()
    for l in lines:
        lst.append(l.strip('\n'))
    print(len(lst),lst)

def part1(arr,testing=False):
    r,c = 1,1 #start on 5 button
    output = ''
    for line in arr:
        for p in line:
            d = p[0] #direction letter
            if d == 'U' and r > 0:
                r -= 1
            if d == 'D' and r < 2:
                r += 1
            if d == 'L' and c > 0:
                c -= 1
            if d == 'R' and c < 2:
                c += 1
        output += str(GRID[r][c])
    return output

def part2(arr):
    r, c = 2,0  # start on 5 button
    output = ''
    for line in arr:
        for p in line:
            d = p[0]  # direction letter
            if d == 'U' and r > 0 and GRID2[r-1][c] != 0:
                r -= 1
            if d == 'D' and r < 4:
                print(r,c)
                if GRID2[r+1][c] != 0:
                    r += 1
            if d == 'L' and c > 0 and GRID2[r][c-1] != 0:
                c -= 1
            if d == 'R' and c < 4:
                if GRID2[r][c+1] != 0:
                 c += 1
        output += str(GRID2[r][c])
    return output

#print(part1(lst))
print(part2(lst))
print("Time (secs):",time.time()-starting_time)