# 11055 가장 큰 증가 부분 수열
"""
아이디어 : 11053과 똑같다. 다만, 기준이 합으로 바뀜.
따라서, 크기를 비교하는 것은 같지만, dp의 합의 크기를 비교한다는 점에서는 의미가 다르다.
"""
"""
import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))

# dp = A는 A와 dp가 같은 리스트를 가리키므로 안됨!!
dp = [0] * n
for i in range(n):      # dp의 원소를 A배열과 맞춤.
    dp[i] = A[i]

for i in range(1, n):
    for j in range(i):
        if A[i] > A[j] and dp[j] + A[i] > dp[i]:
            dp[i] = dp[j] + A[i]
print(dp)
print(max(dp))
"""


""" 백준코드 """
n = int(input())
A = list(map(int, input().split()))

dp = [0] * 1001
for i in A:
    dp[i] = max(dp[:i]) + i     # 자기자신(A의 원소)보다 작은 부분에서 최대값을 구한 후, + i(자기자신 만큼 더함)
print(max(dp))