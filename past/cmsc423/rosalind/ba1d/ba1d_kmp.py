#!/usr/bin/env python

import sys

try:
    data = open(sys.argv[1], "r")
except IOError:
    print "No text file found as name given in script argument."
    quit()

lines = data.readlines()
pattern = lines[0]
del lines[0]
text = "".join(line.strip("\n") for line in lines)

final = [] 
matches = []

for i,c in enumerate(text):
    final.append(0)
    if i > 0:
        for j,n in enumerate(matches):
            if n < len(pattern) and c == pattern[n]:
                matches[j] += 1
            else:
                matches[j] = 0
        
        if c == pattern[0]:
            matches.append(1)

        if len(matches) > 0:
            final[i] = max(matches)

    while 0 in matches: matches.remove(0)

result = [i for i, x in enumerate(final) if x == (len(pattern) - 1)]

result = " ".join(map(str, result))
print result

data.close()
