import sys
input = sys.stdin.readline

N = int(input())
distance = [list(map(int, input().split())) for _ in range(N)]
print(distance)

dp = [[0]*(1<<N) for _ in range(N)]


def dp(i, j):
    if dp[i][j] != 0:
        return dp[i][j]



print(dp)