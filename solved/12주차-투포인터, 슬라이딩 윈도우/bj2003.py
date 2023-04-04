# 2003 수들의 합 2
"""
    다시 풀어보기
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

start = -1
end = 0
ans = 0
sum_subset = 0
while start <= end and end < N:
    start += 1
    while sum(nums[start:end+1]) <= M:
        end += 1
        if end == N:
            break
    if sum(nums[start:end]) == M:
        ans += 1

print(ans)