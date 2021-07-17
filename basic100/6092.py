# [기초-리스트] 이상한 출석 번호 부르기1(설명)(py)

# Constraint
# 0. input: 1 <= n <= 10000
# 1. input: 1 <= n numbers <= 23

n = int(input())
n_list = list(map(int, input().split()))

result = [0] * 23

for i in n_list:
    result[i-1] += 1

print(*result)