# [기초-종합] 수 나열하기2(py)

# Constraint
# 0. input: 0 <= a, r, n <= 10

a, r, n = map(int, input().split())

# print(a * r ** (n-1))

result = a
for i in range(1, n):
    result *= r

print(result)