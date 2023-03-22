# 9084 동전
"""
아이디어 : 중복 없는(순서만 다른것은 한번만셈) 숫자의 합
이 문제에서도 순서만 다른 것은 한번으로 치기 때문에, coin을 기준으로 1부터 M까지 계산한다.
i원은 i - coin + coin 인 점을 이용한다.
dp[0] = 1로 초기화 시켜야한다. coin = 0 + coin => 1가지 방법
"""
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    dp = [0] * (M+1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, M+1):
            dp[i] += dp[i - coin]
    print(dp[-1])
