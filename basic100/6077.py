# [기초-종합] 짝수 합 구하기(설명)(py)

# Constraint
# 0. input: 1 <= n <= 100

print(sum([i for i in range(int(input()) + 1) if i % 2 == 0]))