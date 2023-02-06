# 11051 이항 계수 2
"""
    이항 계수 == 조합(순서가 없음)
    아이디어 : nCk = n-1Ck + n-1Ck-1 임을 이용하여 구한다.
    즉, n개 중 k를 뽑는 가짓수는 n-1개 중 k개를 이미 다 뽑은 경우 + n-1개 중 k-1개를 뽑고 마지막 k번째를 n을 뽑는 경우
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

if k == 0:
    print(1)    # 아무것도 안 뽑는 경우도 1가지로 센다.
    exit(0)

dp = [[0] * (n+1) for _ in range(k+1)]
for i in range(1, n+1):
    dp[1][i] = i

for i in range(2, k+1):
    for j in range(1, n+1):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j-1]) % 10007
print(dp[-1][-1])

"""
# 이항계수의 정리를 이용
# nCk = n! / ((n-k)! * k!)
N,K=map(int,input().split())
UP=1
DOWN=1
for i in range(K):
    UP*=(N-i)
    DOWN*=(i+1)
print((UP//DOWN)%10007)
"""