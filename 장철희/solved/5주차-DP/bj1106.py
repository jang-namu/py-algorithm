# 1106 호텔
"""
아이디어 : 이 문제는 코스트를 정수배만큼 늘려 홍보를 여러번 할 수 있다는게 특징이다.
dp에는 각 인덱스는 유치한 고객수를 의미하고 해당하는 값은 최소비용을 의미한다.
최소비용을 구하기 위해 초기 dp를 10만으로 초기화하여 min()으로 비교한다.
문제어서 "적어도 C명"을 유치하는 최소 비용에 집중하여, C명 이상 유치했을 경우 최소비용을 구한다.
따라서 dp 리스트는 최대 1101의 크기를 가진다.
dp[0]은 0으로 초기화해야 정상적인 계산이 가능하다. dp[i-customer] + cost
"""
import sys
input = sys.stdin.readline

C, N = map(int, input().split())
catalog = list(tuple(map(int, input().split())) for _ in range(N))
dp = [100000] * 1101
dp[0] = 0

for cost, customer in catalog:
    for i in range(1, 1101):
        dp[i] = min(dp[i-customer] + cost, dp[i])

print(dp)
print(min(dp[C:]))