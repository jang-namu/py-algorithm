# 3067 Coins
"""
아이디어 : 앞에서 많이 풀었던 문제와 같다. 그저 coin으로 만들 수 있는 경우를 뽑아주면된다.
            중복은 포함하지 않으므로 coin을 기준으로 coin~M+1을 만드는 방법을 센다.
"""
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    dp = [0] * (M+1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, M+1):
            dp[i] += dp[i-coin]

    print(dp[-1])