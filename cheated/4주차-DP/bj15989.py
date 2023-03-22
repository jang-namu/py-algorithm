# 15989 1, 2, 3 더하기 4
import sys
input = sys.stdin.readline

# 모든 수는 1만 가지고 만들 수 있는 경우의 수가 하나 존재한다.
dp = [1] * 10001
# 2가 추가된 경우를 더해한다.
for i in range(2, 10001):
    dp[i] += dp[i-2]
# 3이 추가된 경우를 더해준다.
for i in range(3, 10001):
    dp[i] += dp[i-3]

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])