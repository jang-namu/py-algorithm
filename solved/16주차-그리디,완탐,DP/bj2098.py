# 2098 외판원 순회
import sys
input = sys.stdin.readline

N = int(input())
cities = [[input().split()] for _ in range(N)]
dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = min(dp[i-1][j] + cities[j][]