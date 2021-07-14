# [기초-종합] 주사위 2개 던지기(설명)(py)

# Constraint
# 0. input: 1 <= n, m <= 10

n, m = map(int, input().split())

for i in range(1, n + 1):
    for j in range(1, m + 1):
        print(i, j)