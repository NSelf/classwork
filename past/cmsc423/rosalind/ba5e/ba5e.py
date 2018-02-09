#!/usr/bin/env python
'''Read blosum into a large map
string alignment matrix is an n+1 * m+1, dashes as x = 0, y = 0
make input all caps
'''
import sys

try:
    f = open(sys.argv[1], 'r')
except IOError:
    print 'Could not find text file named \"{0}\"'.format(sys.argv[1])
    quit()

lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip('\n')

s1 = lines[0]
s2 = lines[1]

sigma = 5
blosum_key = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P',
 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
blosum_values =[
[4, 0, -2, -1, -2, 0, -2, -1, -1, -1, -1, -2, -1, -1, -1, 1, 0, 0, -3, -2],
[0, 9, -3, -4, -2, -3, -3, -1, -3, -1, -1, -3, -3, -3, -3, -1, -1, -1, -2, -2],
[-2, -3, 6, 2, -3, -1, -1, -3, -1, -4, -3, 1, -1, 0, -2, 0, -1, -3, -4, -3],
[-1, -4, 2, 5, -3, -2, 0, -3, 1, -3, -2, 0, -1, 2, 0, 0, -1, -2, -3, -2],
[-2, -2, -3, -3, 6, -3, -1, 0, -3, 0, 0, -3, -4, -3, -3, -2, -2, -1, 1, 3],
[0, -3, -1, -2, -3, 6, -2, -4, -2, -4, -3, 0, -2, -2, -2, 0, -2, -3, -2, -3],
[-2, -3, -1, 0, -1, -2, 8, -3, -1, -3, -2, 1, -2, 0, 0, -1, -2, -3, -2, 2],
[-1, -1, -3, -3, 0, -4, -3, 4, -3, 2, 1, -3, -3, -3, -3, -2, -1, 3, -3, -1],
[-1, -3, -1, 1, -3, -2, -1, -3, 5, -2, -1, 0, -1, 1, 2, 0, -1, -2, -3, -2],
[-1, -1, -4, -3, 0, -4, -3, 2, -2, 4, 2, -3, -3, -2, -2, -2, -1, 1, -2, -1],
[-1, -1, -3, -2, 0, -3, -2, 1, -1, 2, 5, -2, -2, 0, -1, -1, -1, 1, -1, -1],
[-2, -3, 1, 0, -3, 0, 1, -3, 0, -3, -2, 6, -2, 0, 0, 1, 0, -3, -4, -2],
[-1, -3, -1, -1, -4, -2, -2, -3, -1, -3, -2, -2, 7, -1, -2, -1, -1, -2, -4, -3],
[-1, -3, 0, 2, -3, -2, 0, -3, 1, -2, 0, 0, -1, 5, 1, 0, -1, -2, -2, -1],
[-1, -3, -2, 0, -3, -2, 0, -3, 2, -2, -1, 0, -2, 1, 5, -1, -1, -3, -3, -2],
[1, -1, 0, 0, -2, 0, -1, -2, 0, -2, -1, 1, -1, 0, -1, 4, 1, -2, -3, -2],
[0, -1, -1, -1, -2, -2, -2, -1, -1, -1, -1, 0, -1, -1, -1, 1, 5, 0, -2, -2],
[0, -1, -3, -2, -1, -3, -3, 3, -2, 1, 1, -3, -2, -2, -3, -2, 0, 4, -3, -1],
[-3, -2, -4, -3, 1, -2, -2, -3, -3, -2, -1, -4, -4, -2, -3, -3, -2, -3, 11, 2],
[-2, -2, -3, -2, 3, -3, 2, -1, -2, -1, -1, -2, -3, -1, -2, -2, -2, -1, 2, 7],
]

matrix = [[0 for y in range(0, len(s1) + 1)] for x in range(0, len(s2) + 1)]
moves = [ [] for x in range(0, len(s2))]

#The above 2D list generation includes the additional zero row and zero column
for y in range(0, len(s1) + 1):
    matrix[0][y] = y * -sigma
for x in range(0, len(s2) + 1):
    matrix[x][0] = x * -sigma

# for i in matrix:
#     print i
for x in range(1, len(matrix)):
    for y in range(1, len(matrix[x])):
        s1_letter = blosum_key.index(s1[y-1])
        s2_letter = blosum_key.index(s2[x-1])
        # print (s1[y-1],s2[x-1])

        left_score = (matrix[x][y-1]) - sigma
        up_score = (matrix[x-1][y]) - sigma
        diag_score = (matrix[x-1][y-1]) + blosum_values[s1_letter][s2_letter]

        matrix[x][y] = max(left_score, up_score, diag_score)
        if matrix[x][y] == left_score:
            moves[x - 1].append("Right")
        elif matrix[x][y] == up_score:
            moves[x - 1].append("Down")
        else:
            moves[x - 1].append("Diag")

max_length = matrix[-1][-1]

for i in matrix:
    print i
for i in moves:
    print i
x = len(moves) - 1
y = len(moves[0]) - 1
output_s1 = ""
output_s2 = ""
while x >= 0 and y >= 0:
    print (x,y)
    # for i in moves:
    #     print i
    print moves[x][y]
    if moves[x][y] == "Diag":
        output_s1 = s1[y] + output_s1
        output_s2 = s2[x] + output_s2
        x -= 1
        y -= 1
        print (s1[y], s2[x])
    elif moves[x][y] == "Down":
        output_s1 = '-' + output_s1
        output_s2 = s2[x] + output_s2
        x -= 1
        print (s2[x])
    elif moves[x][y] == "Right":
        output_s1 = s1[y] + output_s1
        output_s2 = '-' + output_s2
        y -= 1
        print (s1[y])
for remainder_y in range(y, -1, -1):
    output_s1 = s1[y] + output_s1
for remainder_x in range(x, -1, -1):
    output_s2 = s2[x] + output_s2
output_s1 = ('-' * (x-y)) + output_s1
output_s2 = ('-' * (y-x)) + output_s2

print max_length
print output_s1
print output_s2
