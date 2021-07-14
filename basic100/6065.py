# [기초-조건/선택실행구조] 정수 3개 입력받아 짝수만 출력하기(설명)(py)

# Constraint
# 0. input: 0 <= a, b, c <= 2147483647

input_list = list(map(int, input().split()))

for element in input_list:
    if element % 2 == 0:
        print(element)