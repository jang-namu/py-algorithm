# 1021 회전하는 큐
"""
    단순 구현으로 해결. 양끝점과 원하는 값의 거리 비교
"""
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
obj = list(map(int, input().split()))

num = deque(i for i in range(1, N + 1))

count = 0
for ele in obj:
    if num[0] == ele:
        num.popleft()
        continue
    idx = num.index(ele) + 1
    length = len(num)
    if idx <= length // 2 + 1:
        for _ in range(idx-1):
            num.append(num.popleft())
        count += idx - 1
    else:
        for _ in range(length - idx + 1):
            num.appendleft(num.pop())
        count += length - idx + 1
    num.popleft()

print(count)