#!/usr/bin/env python

import sys

def cyclospectrum(peptide):
    doubled = peptide + peptide
    spectrum = [0] + peptide[:]
    for i in range(0, len(peptide)):
        for j in range(1, len(peptide) - 1):
            spectrum.append(sum(doubled[i:i+j+1]))
    spectrum.append(sum(peptide))
    result = sorted(spectrum)
    return result

def linearspectrum(peptide):
    spectrum = [0] + peptide[:]
    for i in range(0, len(peptide)):
        for j in range(1, len(peptide) - 1):
            spectrum.append(sum(peptide[i:i+j]))
    spectrum.append(sum(peptide))
    result = sorted(spectrum)
    print result
    return result

def consistent(peptide):
    return set(linearspectrum(e)).issubset(set(data))


try:
    f = open(sys.argv[1], 'r')
except IOError:
    print 'Could not find text file named \"{0}\"'.format(sys.argv[1])
    quit()

lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip('\n')
if lines[0] == 'Input':
    data = map(int, lines[1].split(' '))
    answer = lines[3]
    targetMass = data[-1]
else:
    data = map(int, lines[0].split(' '))
    targetMass = data[-1]


aminos = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131,
137, 147, 156, 163, 186]

peptides = [[a] for a in list(aminos)]
results = []

while len(peptides) > 0:
    print "# of candidate peptides remaining after bound: ", len(peptides)
    expand = []
    trim = []
    for p in peptides:
        for a in aminos:
            expand.append(p + [a])

    for e in expand:
        if sum(e) == targetMass:
            if cyclospectrum(e) == data:
                results.append(e)
        elif consistent(e):
            # print e
            # print data
            trim.append(e)
        # else:
        #     print "TRIMMED"
    peptides = trim


answer = []
for i in results:
    answer.append("-".join(map(str, i)))
answer = " ".join(answer)
print "answer: ", answer
