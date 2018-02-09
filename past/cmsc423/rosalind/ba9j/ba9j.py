#!/usr/bin/env python3

import sys

try:
    f = open(sys.argv[1], 'r')
except IOError:
    print('Could not find text file named ' + sys.argv[1])
    quit()

lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip('\n')

data = lines[0]

def find_nth(str, c, n):
    # print(str, c, n)
    if n > 0:
        return find_nth(str[(str.index(c) + 1):], c, n - 1) + str.index(c) + 1
    else:
        return str.index(c)

bwml = data
bwmf = sorted(bwml)

rank = []
counts = {}
for i,c in enumerate(bwml):
    if c not in counts.keys():
        counts[c] = 0
    else:
        counts[c] += 1
    rank.append(counts[c])

t = []
index = 0
while len(t) < len(data):
    # print(index, bwmf[index], bwml[index], rank[index])
    t.append(bwmf[index])
    index = find_nth(bwmf, bwml[index], rank[index])
t.reverse()
print(''.join(t))
