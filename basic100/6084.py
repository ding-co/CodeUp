# [기초-종합] 소리 파일 저장용량 계산하기(py)

# Constraint
# 0. input: 1 <= h <= 48,000
# 1. input: 1 <= b <= 32 (8의 배수)
# 2. input: 1 <= c <= 5
# 3. input: 1 <= s <= 6,000

h, b, c, s = map(int, input().split())

result = (h * b * c * s) / (8 * 1024 * 1024)

print("%.1f MB"%result)