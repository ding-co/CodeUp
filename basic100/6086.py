# [기초-종합] 거기까지! 이제 그만~(설명)(py)

# Constraint
# 0. input: 1 <= n <= 100,000,000

n = int(input())

sum = 0
i = 1
while sum < n:
    sum += i
    i += 1

print(sum)
