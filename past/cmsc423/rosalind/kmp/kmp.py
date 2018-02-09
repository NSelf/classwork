#!/usr/bin/env python

import sys

try:
    data = open(sys.argv[1], "r")
except IOError:
    print "No text file found as name given in script argument."
    quit()

lines = data.readlines()
del lines[0]
text = "".join(line.strip("\n") for line in lines)

final = [] 
matches = []

for i,c in enumerate(text):
    final.append(0)
    if i > 0:
        for j,n in enumerate(matches):
            if c == text[n]:
                matches[j] += 1
            else:
                matches[j] = 0
        
        if c == text[0]:
            matches.append(1)

        if len(matches) > 0:
            final[i] = max(matches)

    while 0 in matches: matches.remove(0)

result = " ".join(map(str, final))

o = open("output.txt", "w+")
o.write(result)

data.close()
o.close()
