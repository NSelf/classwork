#!/usr/bin/env python

import sys

str = "ABBABABA$"

iter = []

for i in range(0, len(str)-1):
    iter.append([str[i]])
    for j in range(i, i + len(str)):
        iter[i].append(str[j%(len(str))])
strings = []
for i in iter:
    strings.append(''.join(i))
    print i

strings.sort()

for s in strings:
    print s
