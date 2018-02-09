#!/usr/bin/env python3

import sys, math

class Node:
    def __init__(self, s, l, parent, l_child, r_child):
        self.parent = parent
        self.l_child = l_child
        self.r_child = r_child
        self.seq = s
        self.s_len = l
        self.matrix = { 'A':[0] * self.s_len,
                        'C':[0] * self.s_len,
                        'G':[0] * self.s_len,
                        'T':[0] * self.s_len}
        if self.seq != "":
            for i,c in enumerate(self.seq):
                for k in self.matrix.keys():
                    if k == c:
                        self.matrix[k][i] = 0
                    else:
                        self.matrix[k][i] = math.inf

def calc_matrix(n):
    for i in range(0, n.s_len):
        for k in n.matrix.keys():
            l_candidates = [n.l_child.matrix[lk][i] + (0 if lk == k else 1) for lk in n.l_child.matrix.keys()]
            r_candidates = [n.r_child.matrix[rk][i] + (0 if rk == k else 1) for rk in n.r_child.matrix.keys()]
            n.matrix[k][i] = min(l_candidates) + min(r_candidates)

def calc_seq(n):
    for i in range(0, n.s_len):
        local_min = (None, math.inf)
        for k in n.matrix.keys():
            if n.matrix[k][i] < local_min[1]:
                local_min = (k, n.matrix[k][i])
        if n.parent != None:
            if n.matrix[n.parent.seq[i]][i] - 1 < local_min[1]:
                # print(i, local_min)
                local_min = (n.parent.seq[i], n.matrix[n.parent.seq[i]][i] - 1)
                # print(local_min)
        n.seq += local_min[0]

def hamming(s1, s2):
    total = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            total += 1
    return total


try:
    f = open(sys.argv[1], 'r')
except IOError:
    print('Could not find text file named ' + sys.argv[1])
    quit()
except IndexError:
    print('Usage: ba7f.py <input-file>')
    quit()

lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip('\n')

n = int(lines[0])
seq_len = len(lines[1][3:])
t = [0] * ((int(lines[0]) * 2) - 1)

for i in range(len(t) - 1, -1, -1):
    if i >= (len(t) - n):
        s = lines[i - (len(t) - n) + 1]
        t[i] = Node(s[3:], seq_len, None, None, None)
    else:
        t[i] = Node("", seq_len, None, t[i * 2 + 1], t[i * 2 + 2])

for i in range(1, len(t)):
    t[i].parent = t[math.floor((i - 1)/2)]

#Calculate non-leaf node matrices
for i in range(n - 2, -1, -1):
    calc_matrix(t[i])
    # print(t[i].matrix)

for e in t:
    if e.l_child != None:
        print("node: " + str(t.index(e)) + " l_child: " + str(t.index(e.l_child)) + " r_child: " + str(t.index(e.r_child)))

    if e.parent != None:
        print("node: " + str(t.index(e)) + " parent: " + str(t.index(e.parent)))

#Backtrack and generate strings
for i in range(0, len(t) - n):
    calc_seq(t[i])
    # print(t[i].seq)



result = [0]

# t[2].seq = "ATGGACTA"

for e in t:
    if e.l_child != None:
        print("node: " + e.seq + " " + str(t.index(e)) + " l_child: " + e.l_child.seq + " " + str(t.index(e.l_child)) + " r_child: " + e.r_child.seq + " " + str(t.index(e.r_child)))
        result.append(e.seq + "->" + e.l_child.seq + ":" + str(hamming(e.seq, e.l_child.seq)))
        result[0] += hamming(e.seq, e.l_child.seq)
    if e.r_child != None:
        result.append(e.seq + "->" + e.r_child.seq + ":" + str(hamming(e.seq, e.r_child.seq)))
        result[0] += hamming(e.seq, e.r_child.seq)
    if e.parent != None:
        print("node: " + e.seq + " " + str(t.index(e)) + " parent: " + e.parent.seq + " " + str(t.index(e.parent)))
        result.append(e.seq + "->" + e.parent.seq + ":" + str(hamming(e.seq, e.parent.seq)))
        result[0] += hamming(e.seq, e.parent.seq)

result[0] /= 2
result[0] = int(result[0])

for l in result:
    print(l)
