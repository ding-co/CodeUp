# [기초-논리연산] 참/거짓이 서로 다를 때에만 참 출력하기(설명)(py)

# Constraint

a, b = map(int, input().split())

print(True if (a and (not b) or ((not a) and b)) else False)