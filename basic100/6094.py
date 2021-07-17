# [기초-리스트] 이상한 출석 번호 부르기3(py)

# Constraint
# 0. input: 1 <= n <= 10000
# 1. input: k

n = int(input())
k_list = list(map(int, input().split()))

print(min(k_list))