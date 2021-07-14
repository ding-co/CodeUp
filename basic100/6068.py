# [기초-조건/선택실행구조] 점수 입력받아 평가 출력하기(설명)(py)

# Constraint
# 0. input: 0 <= n <= 100

n = int(input())

if 90 <= n <= 100:
    print("A")
elif 70 <= n:
    print("B")
elif 40 <= n:
    print("C")
else:
    print("D")