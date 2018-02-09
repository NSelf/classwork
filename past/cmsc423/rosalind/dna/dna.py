#!/usr/bin/env python

data = open("rosalind_dna.txt", "r")

seq = data.read()

print "Data string is: " + seq

ct = [0, 0, 0, 0]

for n in seq:
    if n == "A":
        ct[0]+=1
    elif n == "C":
        ct[1]+=1
    elif n == "G":
        ct[2]+=1
    elif n == "T":
        ct[3]+=1

print ct  

data.close()

