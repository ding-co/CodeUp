# [기초-3항연산] 정수 3개 입력받아 가장 작은 값 출력하기(설명)(py)

# Constraint
# 0. input: -2147483648 <= a, b, c <= +2147483648

a, b, c = map(int, input().split())

print((a if a < c else c) if  a < b else (b if b < c else c))