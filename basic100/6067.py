# [기초-조건/선택실행구조] 정수 1개 입력받아 분류하기(설명)(py)

# Constraint
# 0. input: -2147483648 <= n <= +2147483647

n = int(input())

if n < 0:
    print("A" if (n % 2 == 0) else "B")

elif n > 0:
    print("C" if (n % 2 == 0) else "D")

else:
    pass