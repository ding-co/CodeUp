# [기초-리스트] 이상한 출석 번호 부르기2(py)

# Constraint
# 0. input: 1 <= n <= 10000
# 1. input: 1 <= k <= 23

n = int(input())
k_list = list(map(int, input().split()))

for k in reversed(k_list):
    print(k, end = " ")