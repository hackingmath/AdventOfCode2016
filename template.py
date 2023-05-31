# Advent of Code 2016 Day 9
# https://adventofcode.com/2016/day/9

import time
#from random import randint
from itertools import combinations

starting_time = time.time()

with open('day09.txt') as f:
    lst = list()
    lines = f.readlines()
    lines = [x.strip("\n") for x in lines]
    print(len(lines),lines)

def part1(testing=False):
    pass

def part2():
    pass

#print(part1())
#print(part2())
print("Time (secs):",time.time()-starting_time)