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

def part1(arr,testing=False):
    print(arr)
    in_parens = False
    data_section = False
    output = ''
    end_repeat = 1000
    for i,c in enumerate(arr):#lines[0]):
        print("character:",c)
        if c == '(' and not data_section:
            start = i+1
            in_parens = True
        if c == ')' and not data_section:
            end = i
            in_parens = False
            numstr = [int(x) for x in arr[start:end].split('x')]
            print("numstr",numstr)
            numchars = numstr[0]
            numrepeats = numstr[1]
            repeat_start = i + 1
            data_section = True
            end_repeat = i + 1 + numchars*numrepeats
            to_be_repeated = arr[repeat_start:repeat_start+numchars]
            print("to be repeated:",to_be_repeated)
            output += to_be_repeated*numrepeats
            if i == end_repeat:
                data_section = False
        elif in_parens == False and not data_section:
            output += c

    print('output:',output)

def part2():
    pass

testlines = 'A(1x5)BC'
part1(testlines)
#print(part2())
print("Time (secs):",time.time()-starting_time)