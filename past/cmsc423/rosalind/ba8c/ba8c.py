#!/usr/bin/env python

import sys
from scipy.spatial import distance

try:
    f = open(sys.argv[1], 'r')
except IOError:
    print('Could not find text file named ' + sys.argv[1])
    quit()

lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip('\n')
k = int(lines[0].split()[0])
m = int(lines[0].split()[1])
data = []
for line in lines[1:]:
    data.append([float(x) for x in line.split()])


centers = data[0:k]
new_centers = []
points = data
v_cells = {}

def centroid(points):
    centroid = []
    for dimension in zip(*points):
        centroid.append(round(sum(dimension)/len(dimension), 3))
    return centroid

def v_regroup(centers, points):
    cells = {}
    for p in points:
        parent = None
        min_dist = sys.maxint
        for c in centers:
            if tuple(c) not in cells:
                cells[tuple(c)] = []
            dist = distance.euclidean(p, c)
            if dist < min_dist:
                parent = c
                min_dist = dist
        cells[tuple(parent)].append(p)
    return cells


while (centers != new_centers):
    if (new_centers != []):
        centers = new_centers
    v_cells = v_regroup(centers, points)
    new_centers = []
    for k,v in v_cells.iteritems():
        if v != []:
            new_centers.append(centroid(v))
        else:
            new_centers.append(list(k))

for c in centers:
    print(' '.join(map(str, c)))
