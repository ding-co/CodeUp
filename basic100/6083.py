# [기초-종합] 빛 섞어 색 만들기(설명)(py)

# Constraint
# 0. input: 0 <= r,g,b <= 127

r, g, b = map(int, input().split())

count = 0

for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
            count += 1

print(count)