# [기초-3항연산] 정수 2개 입력받아 큰 값 출력하기(설명)(py)

# Constraint
# 0. input: -2147483648 <= a, b <= +2147483647

a, b = map(int, input().split())

print(a if(a > b) else b)