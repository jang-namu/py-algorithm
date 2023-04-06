# 1806 부분합
"""
    N의 크기가 10만이므로, O(n^2)으로는 못 푼다.
    투포인터를 사용하면 O(n)시간에 풀 수 있다.
    부분합을 구하고, S 이상일 때, min으로 최소 길이를 구한다.
"""
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

low = 0
high = 0
total = 0
length = 1e10
while True:
    while total < S and high < N:
        total += nums[high]
        high += 1
    if total >= S:
        length = min(length, high-low)

    total -= nums[low]
    low += 1
    if low == N:
        break
print(length if length != 1e10 else 0)