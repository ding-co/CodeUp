# [기초-논리연산] 둘 다 거짓일 경우만 참 출력하기(py)

# Constraint

a, b = map(int, input().split())

print(True if not a and not b else False)