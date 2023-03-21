# 1535 안녕
"""
아이디어 : 14693하고 같다. 1~N번까지 사람을 한명씩 추가하며
, 소모되는 체력을 0부터 99까지 최대 얻을 수 있는 기쁨을 구한다.
dp[i] = 체력 i를 소모했을 때 최대 기쁨
"""
import sys
input = sys.stdin.readline
N = int(input())
health = list(map(int, input().split()))
happy = list(map(int, input().split()))
"""
dp = [[0] * 100 for _ in range(N+1)]

for i in range(1, N+1):
    heart, emotion = health[i-1], happy[i-1]
    for j in range(100):
        if j - heart >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-heart] + emotion)
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1])
"""

# 1차원 배열로 해결
dp = [0] * 100
for i in range(1, N+1):
    heart, emotion = health[i-1], happy[i-1]
    for j in range(99, heart - 1, -1):
        if dp[j-heart] + emotion > dp[j]:
            dp[j] = dp[j-heart] + emotion
print(dp)
print(dp[-1])