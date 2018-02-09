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
metadata = lines[0].split(" ")
k = int(metadata[0])
t = int(metadata[1])
motifs = []
bestMotifs = []
minScore = 100
for i in range(len(lines[1]) - k):
	profile = {"A" : 0, "C" : 0, "G" : 0, "T" : 0}
	motifs.append(lines[1][i:i + k])
	for j in range(2, t + 1): #to include last line, since the first is metadata
		
		#profiling motifs
		consensus = ""
		for j in range(len(motifs[0])):
			for i in range(len(motifs[i][j])):
				maxChar = ''
				maxCharCount = 0
				profile[motifs[i][j]] += 1
				if profile[motifs[i][j]] > maxCharCount:
					maxCharCount = profile[motifs[i][j]]
                                        maxChar = motifs[i][j]
                        
                        consensus += maxChar

		bestMatch = [0, "DEFAULT"]

		maxProb = 0
		maxMotif = motifs[0]
		for m in motifs:
			for c in m:
    			        curProb = 1
				curProb *= profile[c]
				if curProb >= maxProb:
					maxProb = curProb
					maxMotif = m
		
		motifs.append(maxMotif)
		
