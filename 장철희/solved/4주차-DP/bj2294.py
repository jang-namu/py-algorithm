# 2294 동전 2
"""
아이디어 : 숫자문제와 비슷함. 각 숫자에 대해 쓰는 동전 수를 최소화하는 dp를 생성한다.
예외처리 : 못 만들 경우, !!동전크기가 값보다 더 큰 경우 인덱싱에러!!
수정사항 : dp를 처음에 10001(최소가치 동전 1로 1만을 만드려면 1만개 필요)로 채우면,
dp[i-coin] != 0과 dp[i] != 0을 매번 조건문을 검사하지 않아도 된다.
"""
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = list(int(input()) for _ in range(n))
coins.sort()
for i in range(n):
    if coins[i] > k:
        coins = coins[:i]
        break
MIN = coins[0]

dp = [10001] * (k+1)
dp[MIN] = 1

for coin in coins:
    dp[coin] = 1
    for i in range(coin, k+1):
        dp[i] = min(dp[i-coin] + 1, dp[i])

if dp[k] != 10001:
    print(dp[k])
else:
    print(-1)
"""
dp = [0] * (k+1)
dp[MIN] = 1

for coin in coins:
    dp[coin] = 1
    for i in range(coin, k+1):
        if dp[i-coin] != 0:
            dp[i] = min(dp[i-coin] + 1, dp[i]) if dp[i] != 0 else dp[i-coin] + 1

if dp[k] != 0:
    print(dp[k])
else:
    print(-1)
"""

# 백준 깔끔한 코드
"""N,M = map(int, input().split())

monList = []
for i in range(N):
  monList.append(int(input()))

dpList = [10001] * (M+1)
dpList[0] = 0

for i in monList:
  for j in range(i,M+1):
    dpList[j] = min(dpList[j-i]+1, dpList[j])

if dpList[M] == 10001:
  print(-1)
else:
    print(dpList[M])     
"""
