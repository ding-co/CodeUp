# [기초-종합] 16진수 구구단 출력하기(py)

# Constraint

n = input()

for i in range(1, 15 + 1):
    convert_n = int(n, 16)
    print("{:X}*{:X}={:X}".format(convert_n, i, convert_n * i))