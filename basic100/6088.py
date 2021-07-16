# [기초-종합] 수 나열하기1(py)

# Constraint
# 0. input: 0 <= a, d, n <= 100

a, d, n = map(int, input().split())

# print(a + (n - 1) * d)

sum = a
for i in range(1, n):
    sum += d

print(sum)