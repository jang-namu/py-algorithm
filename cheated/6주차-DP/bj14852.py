# 14852 타일 채우기 3
"""
https://foramonth.tistory.com/9
점화식을 정리해서, sum() 이나 for문 등, O(n^2)이 아닌 O(n)으로 풀어냈다.
      dp[x] = 2 * sum(dp[:x - 1]) + dp[x - 2]
            = 2 * dp[x - 1] + 2 * sum(dp[:x - 2]) + dp[x - 2]   => 우변에 + dp[x-3] - dp[x-3]을 취한다.
            = 2 * dp[x - 1] + dp[x - 1] - dp[x - 3] + dp[x - 2]
            = 3 * dp[x - 1] + dp[x - 2] - dp[x - 3]
"""
import sys
MOD = 1000000007
n = int(sys.stdin.readline())

dp = [0] * (1000001)
dp[1], dp[2], dp[3] = 2, 7, 22

for x in range(4, n+1):
    dp[x] = (3 * dp[x - 1] + dp[x - 2] - dp[x - 3]) % MOD

print(dp[n])

"""
# 좀 더 직관적인 해결법
leng = int(input())

memo = [0]*(leng+1)
memo[0:3] = [1, 2, 7]

summemo = 0
for i in range(3, leng+1):
    summemo += memo[i-3]
    memo[i] = (2*memo[i-1] + 3*memo[i-2] + 2*summemo)%1000000007

print(memo[leng]) 
"""

"""
# 내 풀이, 아이디어는 같았으나 이중 for문으로 인한 시간초과.
import sys
MOD = 1000000007
n = int(sys.stdin.readline())

dp = [0] * (n+1)
dp[1], dp[2], dp[3] = 2, 7, 22
for i in range(4, n+1):
    dp[i] = dp[i-1] * 2 + 2
    for j in range(1, i-1):

    dp[i] %= MOD
    
print(dp[-1])
"""