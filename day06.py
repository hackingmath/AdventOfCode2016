# Advent of Code 2016 Day 6
# https://adventofcode.com/2016/day/6

import time
#from random import randint
from itertools import combinations

starting_time = time.time()

with open('day06.txt') as f:
    lst = list()
    lines = f.readlines()
    lines = [x.strip("\n") for x in lines]
    print(len(lines),lines)


def part1(testing=False):
    word = ''
    for p in range(8):
        col = [row[p] for row in lines]
        highest = 0
        recordletter = ''
        for letter in col:
            cnt = col.count(letter)
            if cnt > highest:
                highest = cnt
                recordletter = letter
        word += recordletter
    print(word)

def part2():
    word = ''
    for p in range(8):
        col = [row[p] for row in lines]
        lowest = 500
        recordletter = ''
        for letter in col:
            cnt = col.count(letter)
            if cnt < lowest:
                lowest = cnt
                recordletter = letter
        word += recordletter
    print(word)

#part1()
part2()
print("Time (secs):",time.time()-starting_time)