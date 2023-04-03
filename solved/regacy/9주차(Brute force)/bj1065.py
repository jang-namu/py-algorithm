# 1065 한수
"""
    n이 충분히 작다. -> 4자릿수가 등차수열인지 확인하는데 3번의 연산, 2번의 비교 => 연산횟수가 적으므로 완탐(brute force)
"""

n = int(input())

cnt = 0
for num in range(1, n+1):
    if num < 10:
        cnt += 1
        continue
    num = str(num)
    length = len(num)
    diff = int(num[0]) - int(num[1])
    sign = True
    for j in range(1, len(num)-1):
        if diff != int(num[j]) - int(num[j+1]):
            sign = False
    if sign:
        cnt += 1
print(cnt)