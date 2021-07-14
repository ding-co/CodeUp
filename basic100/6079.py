# [기초-종합] 언제까지 더해야 할까?(py)

# Constraint

n = int(input())

i = 1
sum = 0

while sum < n:
    sum += i
    i += 1

print(i - 1)