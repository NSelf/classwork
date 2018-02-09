#!/usr/bin/env python

import sys

try:
    data = open(sys.argv[1], "r")
except IOError:
    print "No text file found as name given in script arguments."
    quit()

lines = data.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip("\n")
text = lines[0]
k = int(lines[1])
profiles = [map(float, lines[2].split(" ")),
            map(float, lines[3].split(" ")),
            map(float, lines[4].split(" ")),
            map(float, lines[5].split(" "))]
bestMatch = [0, "DEFAULT"]

for i in range(len(text) - k):
    cur = text[i:(i + k)] #Building the k-mer in question.
    curProb = 1.0
    for j,c in enumerate(cur):
        if c == 'A':
            curProb *= profiles[0][j]
        elif c == 'C':
            curProb *= profiles[1][j]
        elif c == 'G':
            curProb *= profiles[2][j]
        elif c == 'T':
            curProb *= profiles[3][j]
    if curProb > bestMatch[0]:
        bestMatch = [curProb, cur]

print bestMatch[1]

