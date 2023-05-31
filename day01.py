# Advent of Code 2016 Day 1
# https://adventofcode.com/2016/day/1

import time
#from random import randint
from itertools import combinations

starting_time = time.time()

with open('day01.txt') as f:
    lst = list()
    lines = f.readlines()
    lst = [str.split(', ') for str in lines][0]
    print(len(lst),lst)

def part1(testing=False):
    direction = 0
    dir_dict = {0:0,1:0,2:0,3:0}
    testlst = ["R5",'L5','R5','R3']
    for step in lst:
        if step[0] == 'R':
            direction = (direction + 1)%4
        elif step[0] == 'L':
            direction = (direction - 1)%4
        dir_dict[direction] += int(step[1:])
    print(dir_dict)
    distance = abs(dir_dict[0]-dir_dict[2]) + abs(dir_dict[1]-dir_dict[3])
    print("distance:",distance)

def part2():
    x,y = 0,0
    direction = 0
    locs = set()
    testlst = ['R8', 'R4', 'R4', 'R8']
    for step in lst:
        if step[0] == 'R':
            direction = (direction + 1)%4
        elif step[0] == 'L':
            direction = (direction - 1)%4

        for i in range(1,int(step[1:])+1):
            if direction == 0:
                y += 1
            elif direction == 1:
                x += 1
            elif direction == 2:
                y -= 1
            elif direction == 3:
                x -= 1
            #print(x,y)
            if (x, y) in locs:
                print("distance:", x + y)
                return
            else:
                locs.add((x, y))


#print(part1())
print(part2())
print("Time (secs):",time.time()-starting_time)