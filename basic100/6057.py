# [기초-논리연산] 참/거짓이 서로 같을 때에만 참 출력하기(설명)(py)

# Constraint

a, b = map(int, input().split())

print(True if (a and b) or (not a and not b) else False)