# 14728 벼락치기
import sys
input = sys.stdin.readline

N, T = map(int, input().split())

def knapsack(N, T):
    dp = [0] * (T+1)
    for _ in range(N):
        k, s = map(int, input().split())
        for i in range(T, k-1, -1):
            dp[i] = max(dp[i], dp[i-k] + s)
    return dp[-1]

print(knapsack(N, T))