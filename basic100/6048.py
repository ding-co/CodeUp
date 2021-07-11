# [기초-비교연산] 정수 2개 입력받아 비교하기1(설명)(py)

# Constraint
# 0. input: -2147483648 <= a, b <= +2147483647

a, b = map(int, input().split())

print(True if a < b else False)