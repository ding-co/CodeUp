# [기초-종합] 그림 파일 저장용량 계산하기(py)

# Constraint
# 0. input: 1 <= w,h <= 1024
# 1. input: b <= 40 (4의 배수)

w, h, b = map(int, input().split())

result = (w * h * b) / (8 * 1024 * 1024)

print("%.2f MB" % result)