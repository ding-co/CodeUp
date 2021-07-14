# [기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기(설명)(py)

# Constraint
# 0. input: a ~ z

input_data = input()

temp = ord('a')

while temp <= ord(input_data):
    print(chr(temp), end = " ")
    temp += 1