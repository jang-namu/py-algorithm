# 2293 동전 1
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = list(int(input()) for _ in range(n))
if min(coin) > k:
    print(0)
    exit(0)

dp = {coin[i]: 1 for i in range(n)}
print(dp)

for value in coin:
    for i in range(min(coin), k+1):
        if (i - value) in dp:
            if i in dp:
                dp[i] += dp.get(i - value, 0)
            else:
                dp[i] = dp.get(i - value, 0)
"""
for i in range(min(coin), k+1):
    for value in coin:
        if (i-value) in dp:
            if i in dp:
                dp[i] += dp.get(i-value, 0)
            else:
                dp[i] = dp.get(i-value, 0)
"""
print(dp)
print(dp[k])