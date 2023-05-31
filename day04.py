# Advent of Code 2016 Day 4
# https://adventofcode.com/2016/day/4

import time
#from random import randint
from itertools import combinations

starting_time = time.time()

with open('day04.txt') as f:
    lst = list()
    lines = f.readlines()
    lines = [x.strip("\n") for x in lines]
    print(len(lines),lines)

def create_checksum(st,testing=False):
    print("st:",st)
    # find index of first number
    n_idx = list()
    for i in range(1, 10):
        try:
            n_idx.append(st.index(str(i)))
        except ValueError:
            pass
    lowest_n = min(n_idx)
    highest_n = lowest_n
    step = 1
    while st[lowest_n+step] in '0123456789':
        highest_n += 1
        step += 1
    if testing:
        print("number indices:",lowest_n,highest_n)
    sector_id = int(st[lowest_n:(highest_n+1)])
    #find checksum between brackets
    openb, closeb = st.index('['), st.index(']')
    checksum = st[(openb + 1):closeb]
    if testing:
        print("checksum:",checksum)
    #find letters with highest frequency
    letters = st[:lowest_n].replace('-', "")
    letterset = set()
    for letter in letters:
        letterset.add(letter)
    letter_dict = {letter: letters.count(letter) for letter in letterset}
    sortedletters = sorted(letter_dict.items(), reverse=True, key=lambda x: x[1])
    #highest count
    highest = sortedletters[0][1]
    #print(highest)
    cs = [] #empty checksum
    lets = dict()
    for i in range(highest,0,-1):
        lets[i] = []
        #find all letters with that frequency
        for p in letterset:
            if letter_dict[p] == i:
                lets[i].append(p)
        #concatenate all letters in order
        cs += sorted(lets[i])
    output = ''.join(cs)
    if testing:
        print("mychecksum:",output[:5])
    # print(st,sortedletters[:5],sector_id,checksum)
    if checksum == output[:5]:
        if testing:
            print("output:", sector_id)
        return sector_id
    else:
        print("output: 0")
        return 0


def part1(testing=False):
    output = 0
    for line in lines:

        output += create_checksum(line,True)
    print(output)

def rotate_string(st,n):
    ALPHA = 'abcdefghijklmnopqrstuvwxyz'
    rotnum = n%26
    output = ''
    for letter in st:
        if letter == '-':
            output += ' '
            continue
        idx = ALPHA.index(letter)
        output += ALPHA[(idx+rotnum)%26]
    return output

def part2(testing=False):
    for st in lines:
        #print("st:", st)
        # find index of first number
        n_idx = list()
        for i in range(1, 10):
            try:
                n_idx.append(st.index(str(i)))
            except ValueError:
                pass
        lowest_n = min(n_idx)
        highest_n = lowest_n
        step = 1
        while st[lowest_n + step] in '0123456789':
            highest_n += 1
            step += 1
        if testing:
            print("number indices:", lowest_n, highest_n)
        sector_id = int(st[lowest_n:(highest_n + 1)])
        # find checksum between brackets
        openb, closeb = st.index('['), st.index(']')
        checksum = st[(openb + 1):closeb]
        letters = st[:lowest_n]#.replace('-', "")
        newstr = rotate_string(letters,sector_id)
        if 'storage' in newstr:
            print(sector_id,rotate_string(letters,sector_id))

#part1()
part2()
print("Time (secs):",time.time()-starting_time)