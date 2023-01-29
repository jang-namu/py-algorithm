# 15988 1, 2, 3 더하기 3
import sys
input = sys.stdin.readline

T = int(input())
n = list(int(input()) for _ in range(T))
dp = [0] * (max(n)+1)
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, max(n)+1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009
for idx in n:
    print(dp[idx])


""" 문제의 모든조건이 9095번과 같다.
    다만, 이 문제에서는 n이 백만까지 커질 수 있다.
    이 문제를 풀기위해 9095에 재귀함수에서 메모이제이션 아이디어를 추가해 재귀가 아닌
    for로 풀어야한다. 재귀함수에 경우 함수호출이 엄청나게 많이 일어난다.
    아래는 시간초과가 됨 
"""
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def makeNum(n):
    if dp[n] != 0:
        return dp[n]
    dp[n] = (makeNum(n-1) + makeNum(n-2) + makeNum(n-3)) % 1000000009
    return dp[n]


T = int(input())
dp = [0] * (10**6+1)
dp[1] = 1
dp[2] = 2
dp[3] = 4
for _ in range(T):
    n = int(input())
    print(makeNum(n))
"""