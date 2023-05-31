# Advent of Code 2016 Day 3
# https://adventofcode.com/2016/day/3

import time
#from random import randint
from itertools import combinations

starting_time = time.time()

with open('day03.txt') as f:
    lst = list()
    lines = f.readlines()
    lines = [x.strip("\n") for x in lines]
    print(len(lines),lines)

def part1(testing=False):
    tris = 0
    not_tris = 0
    is_tri = 0
    for line in lines:
        nums = [int(n) for n in line.split( )]
        nums2 = sorted(nums)
        #s = sum([x for x in nums if x != biggest])
        if nums2[0] + nums2[1] > nums2[2]:#s > biggest:
            tris += 1
            is_tri = True
        else:
            not_tris += 1
            is_tri = False
        #print(nums, s, biggest,is_tri)

    return tris,not_tris

def part2():
    tris = 0
    not_tris = 0
    is_tri = 0
    nums = [[int(n) for n in line.split()] for line in lines]
    nums3 = list()
    for i in range(0,int(len(nums)),3):
        for j in range(3):
            nums3.append([nums[i][j],nums[i+1][j],nums[i+2][j]])
    print(len(nums3),"nums3:",nums3[:12])
    for line in nums3:
        nums2 = sorted(line)
        # s = sum([x for x in nums if x != biggest])
        if nums2[0] + nums2[1] > nums2[2]:  # s > biggest:
            tris += 1
            is_tri = True
        else:
            not_tris += 1
            is_tri = False
        # print(nums, s, biggest,is_tri)

    return tris, not_tris

#print(part1())
print(part2())
print("Time (secs):",time.time()-starting_time)