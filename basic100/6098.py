# [기초-리스트] 성실한 개미(py)

# Constraint
# 0. input: 10 X 10 coord

import sys

input = sys.stdin.readline

curr_coord = []
for i in range(1, 10 + 1):
    input_row = list(map(int, input().split()))
    curr_coord.append(input_row)

start_x, start_y = 1, 1

curr_coord[start_x][start_y] = 9

while True: 
    if (curr_coord[start_x][start_y] == 0): 
        curr_coord[start_x][start_y] = 9 
    elif (curr_coord[start_x][start_y] == 2): 
        curr_coord[start_x][start_y] = 9
        break 
    if ((curr_coord[start_x][start_y + 1] == 1 and curr_coord[start_x + 1][start_y] == 1)):
        break 
    if (curr_coord[start_x][start_y + 1] != 1): 
        start_y = start_y + 1 
    elif (curr_coord[start_x + 1][start_y] != 1): 
        start_x = start_x + 1

for a in curr_coord:
    for b in a:
        print(b, end = " ")
    print()