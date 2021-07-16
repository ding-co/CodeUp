# [기초-종합] 수 나열하기3(py)

# Constraint
# 0. input: -50 <= a, m, d <= 50
# 1. input: 1 <= n <= 10

a, m, d, n = map(int, input().split())

result = a
for i in range(1, n):
    result = result * m + d

print(result)