# [기초-산술연산] 정수 2개 입력받아 자동 계산하기(py)

# Constraint
# 0. input: 0 <= a <= 2147483647 and 0 < b <= 2147483647

num1, num2 = map(int, input().split())

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 // num2)
print(num1 % num2)
print(format((num1 / num2), ".2f"))