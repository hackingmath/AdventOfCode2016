# Advent of Code 2016 Day 7
# https://adventofcode.com/2016/day/7

import time
#from random import randint
from itertools import combinations

starting_time = time.time()

with open('day07.txt') as f:
    lst = list()
    lines = f.readlines()
    lines = [x.strip("\n") for x in lines]
    #print(len(lines),lines)

def palindrome4(st):
    """Returns True if string is palindrome
    4-long with different pairs"""
    return st[0] == st[3] and st[1]==st[2] and st[0] != st[1]

def palindrome3(st):
    """Returns True if string is palindrome
    3-long with different letters"""
    return st[0] == st[2] and st[0] != st[1]

def corresponding3(st):
    return st[1]+st[0]+st[1]

# for s in ['abba','aaaa','xyyx','xyxy']:
#     print(palindrome(s))

def search_single(st):
    """Loops through string, checking if each quadruplet is a
        palindrome. Skips brackets."""
    idx = 0
    while idx < len(st) - 4:
        quad = st[idx:(idx + 4)]
        if '[' in quad:
            idx += quad.index('[') + 1

            # find closing bracket
            while st[idx] != ']':
                quad = st[idx:(idx + 4)]
                if palindrome4(quad):
                    print("fail quad",quad)
                    return False
                idx += 1

        elif palindrome4(quad):
            print("Success!", quad)
            return True
        idx += 1
    return False

def search_string(st,n=3,testing=False):
    """Returns palindrome of length n if found in string"""
    idx = 0
    output = []
    while idx < len(st)-n+1:
        chunk = st[idx:(idx + n)]
        if testing:
            print("searching chunk",chunk)
        if palindrome3(chunk):
            if testing:
                print("chunk:",chunk)
            output.append(chunk)
        idx += 1
    return output

def search_brackets(st,testing=False):
    """Returns strings in brackets"""
    idx = 0
    output = []
    while idx < len(st)-4:
        print("idx:",idx)
        try:
            while st[idx] != '[':
                idx += 1
        except IndexError:
            break
        start = idx + 1
        if testing:
            print("start:",start)
        while st[idx] != ']':
            idx += 1
        idx += 1
        end = idx
        if testing:
            print("end:",end)
        bidx = start
        chars = st[start:end-1]
        if testing:
            print('chars:',chars)
            output.append(chars)
            # corr = corresponding3(trip)
            # if corr in st:
            #     return True
        print("output",output)
        idx += 1
    return output

#search_brackets('vjqhodfzrrqjshbhx[lezezbbswydnjnz]ejcflwytgzvyigz[hjdilpgdyzfkloa]mxtkrysovvotkuyekba',True)
def part1OLD(testing=False):

    successes = 0
    testlines = ['abba[mnop]qrst','abcd[bddb]xyyx','ioxxoj[asdfgh]zxcvbn']
    for st in lines:
        print(st)
        if search_single(st):
            successes += 1

    return successes

def part2OLD():
    successes = 0
    testlines = ['aba[bab]xyz', 'xyx[xyx]xyx', 'aaa[kek]eke','zazbz[bzb]cdb']
    for st in lines:
        print(st)
        chars = search_brackets(st,True)
        print("chars:",chars)
        for chunk in chars:
            pals = search_string(chunk,3,True)
        if len(pals) != 0:
            for trip in pals:
                corr = corresponding3(trip)
                print("corr:",corr)
                if corr in st:
                    successes += 1
    return successes

def part1():
    ans = 0
    testlines = ['abba[mnop]qrst','abcd[bddb]xyyx','ioxxoj[asdfgh]zxcvbn']
    for line in lines:
        print(line)
        in_brackets = False
        abba = [False,False]
        for i,c in enumerate(line):
            if c == '[':
                 in_brackets = True
            elif c == ']':
                in_brackets = False
            elif i+3<len(line) and line[i]==line[i+3] and line[i]!=line[i+1] and line[i+1]==line[i+2] and line[i] not in ['[',']'] and line[i+1] not in ['[',']']:
                abba[in_brackets] = True
        if abba[False] and not abba[True]:
            ans +=1
    print(ans)

def part2():
    ans = 0
    testlines = ['aba[bab]xyz', 'xyx[xyx]xyx', 'aaa[kek]eke','zazbz[bzb]cdb']
    for line in lines:
        print(line)
        in_brackets = False
        aba = {True: set(), False:set()}
        for i,c in enumerate(line):
            if c == '[':
                 in_brackets = True
            elif c == ']':
                in_brackets = False
            elif i+2<len(line) and line[i]==line[i+2] and line[i]!=line[i+1]:# and line[i+1]==line[i+2] and line[i] not in ['[',']'] and line[i+1] not in ['[',']']:
                print(line[i:i+2])
                aba[in_brackets].add(line[i:i+3])
        good = False
        for a,b,c in aba[True]:
            if '{}{}{}'.format(b,a,b) in aba[False]:
                good = True

        if good: ans += 1
    print(ans)

#print(part1OLD()) #104 wrong. it was 105
#part1() #105
part2() #236 too low. Correct: 258
print("Time (secs):",time.time()-starting_time)