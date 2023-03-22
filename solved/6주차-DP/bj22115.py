# 22115 창영이와 커피
"""
아이디어 : 16493, 앞에서 많이 풀었던 knapsack 문제.
coffee를 기준으로 뒤에서부터 계산하는게 핵심(중첩을 피하기위해, 커피는 하나씩 있음)
"""
import sys
input = sys.stdin.readline

_, K = map(int, input().split())
coffees = list(map(int, input().split()))

# 배열을 크게 잡고 속도 위주로 작성한 코드 23.02.04 기준 1등
dp = [101] * (100000+1)
dp[0] = 0

length = 0
for coffee in coffees:
    for i in range(length + coffee, coffee-1, -1):
        if dp[i-coffee] + 1 < dp[i]:
            dp[i] = dp[i-coffee] + 1
    length += coffee
print(dp[K] if dp[K] != 101 else -1)

"""
# 22115 창영이와 커피
import sys
input = sys.stdin.readline

_, K = map(int, input().split())
coffees = list(map(int, input().split()))

dp = [101] * (K+1)
dp[0] = 0
for coffee in coffees:
    for i in range(K, coffee-1, -1):
            dp[i] = min(dp[i-coffee] + 1, dp[i])

print(dp[-1] if dp[-1] != 101 else -1)
"""