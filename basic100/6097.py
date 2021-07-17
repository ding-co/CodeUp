# [기초-리스트] 설탕과자 뽑기(py)

# Constraint
# 0. input: 1 <= h, w <= 100
# 1. input: 1 <= n <= 10
# 2. input: d == 0 or 1
# 3. input: 1 <= x <= 100-h
# 4. input: 1 <= y <= 100-w

h, w = map(int, input().split())
coord = [ [0 for i in range(1, w + 1)] for j in range(1, h + 1) ]
n = int(input())
for _ in range(n):
    l, d, x, y = map(int, input().split())
    for j in range(l):
        if d == 0:
            coord[x - 1][y - 1 + j] = 1
        else:
            coord[x - 1 + j][y - 1] = 1

for a in coord:
    for b in a:
        print(b, end = " ")
    print()    