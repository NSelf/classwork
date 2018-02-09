#!/usr/bin/env python

try:
    f = open("rosalind_ba1f.txt", "r")
    #f = open("test.txt", "r")
except IOError:
    print "No data file found."
    quit()

data = f.readlines()[0]

skew = 0
svalues = []
for c in data:
    svalues.append(skew)
    if c == 'C':
        skew -= 1
    if c == 'G':
        skew += 1
    
svalues.append(skew)

minima = []
for ind,i in enumerate(svalues):
    if i == min(svalues):
        minima.append(ind)

print "svalues: %s" % str(svalues)
print "Indices of minimum skew: \n %s" %  " ".join(map(str, minima))
