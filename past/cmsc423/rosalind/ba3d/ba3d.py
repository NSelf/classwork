#!/usr/bin/env python3

import sys

try:
    f = open(sys.argv[1], 'r')
except IOError:
    print('Could not find text file named ' + sys.argv[1])
    quit()

lines = f.readlines()

k = int(lines[0])
data = lines[1]

debrujin = {}

for i in range(0, len(data) - k):
    start = data[i : i + k - 1]
    end = data[i + 1 : i + k]
    if start in debrujin.keys():
        debrujin[start].append(end)
    else:
        debrujin[start] = [end]

for k in sorted(debrujin.keys()):
    print(k + " -> " + ",".join(sorted(debrujin[k])))
