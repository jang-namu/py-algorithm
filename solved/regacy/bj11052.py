# 11052 카드 구매하기
"""
    아이디어 : n개의 카드를 사는 경우는 n-i개를 산 경우에 i개를 추가로 사는 경우이다.
                dp의 인덱스는 산 카드갯수, 값은 인덱스(갯수)만큼 샀을 때 최대금액
"""
import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

dp = [0] * (n+1)
dp[1] = cards[0]
for i in range(2, n+1):
    for j in range(1, i+1):
        if dp[i] < dp[i-j] + cards[j-1]:
            dp[i] = dp[i - j] + cards[j-1]
print(dp)
print(dp[-1])