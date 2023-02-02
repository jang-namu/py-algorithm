# 12865 평범한 배낭
"""
아이디어 : 각 자리(들수있는무게 0~K)에서 최대한의 value
앞에서부터 할 시, 현재 luggage를 여러개 들어버리는 것과 같이지므로,
뒤에서부터 계산한다.
"""
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
#luggage = list(tuple(map(int, input().split())) for _ in range(N))
#print(luggage)

dp = [0] * (K+1)
for _ in range(N):
    w, v = map(int, input().split())
    for i in range(K, w-1, -1):
        dp[i] = max(dp[i], dp[i-w] + v)
print(dp)
print(dp[-1])