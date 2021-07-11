# [기초-비트시프트연산] 2의 거듭제곱 배로 곱해 출력하기(설명)(py)

# Constraint
# 0. input: 0 <= a, b <= 10

a, b = map(int, input().split())

# left-shifted by b
print(a << b)