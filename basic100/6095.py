# [기초-리스트] 바둑판에 흰 돌 놓기(설명)(py)

# Constraint
# 0. input: 1 <= n (white) <= 10
# 1. input: 1 <= x,y <= 19

n = int(input())
total = [ [0 for i in range(1, 19 + 1)] for j in range(1, 19 + 1) ]
for i in range(n):
    x, y = map(int, input().split())
    if total[x - 1][y - 1] == 0:
        total[x - 1][y - 1] += 1

for a in total:
    print(*a)