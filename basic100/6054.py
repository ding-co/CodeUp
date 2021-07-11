# [기초-논리연산] 둘 다 참일 경우만 참 출력하기(설명)(py)

# Constraint

a, b = map(int, input().split())

print(True if bool(a) and bool(b) else False)