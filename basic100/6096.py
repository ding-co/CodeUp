# [기초-리스트] 바둑알 십자 뒤집기(py)

# Constraint
# 0. input: 19 * 19 
# 1. input: 1 <= n < = 10
# 2. input: reverse coordinate

curr_coord = []
for _ in range(0, 18 + 1):
    curr_coord_row = list(map(int, input().split()))
    curr_coord.append(curr_coord_row)

n = int(input())
for i in range(1, n + 1):
    reverse_coord_x, reverse_coord_y = map(int, input().split())
    for j in range(0, 18 + 1):
        if curr_coord[reverse_coord_x - 1][j] == 0:
            curr_coord[reverse_coord_x - 1][j] = 1
        else:
            curr_coord[reverse_coord_x - 1][j] = 0

        if curr_coord[j][reverse_coord_y - 1] == 0:
            curr_coord[j][reverse_coord_y - 1] = 1
        else:
            curr_coord[j][reverse_coord_y - 1] = 0

for a in curr_coord:
    print(*a)