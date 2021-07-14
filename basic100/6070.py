# [기초-조건/선택실행구조] 월 입력받아 계절 출력하기(설명)(py)

# Constraint
# 0. input: 1 <= n <= 12

month = int(input())

if 3 <= month <= 5:
    print("spring")
elif 6 <= month <= 8:
    print("summer")
elif 9 <= month <= 11:
    print("fall")
else:
    print("winter")