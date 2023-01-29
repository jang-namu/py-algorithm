# 15993 1, 2, 3 더하기 8
"""
아이디어 : 15992와 비슷한데 더 쉬움
이번엔 홀수 짝수만 저장하면된다.
갯수야 n-3, n-2, n-1 에서 모두 하나씩 늘어나는 거기 때문에
매 iteration마다 홀수 짝수를 구해가면서 **위치를 바꿔주면됨**
"""
import sys
input = sys.stdin.readline
MOD = 10**9+9

T = int(input())
n = list(int(input()) for _ in range(T))
MAX = max(n)
dp = list([0, 0] for _ in range(MAX+1))
dp[1] = [1, 0]
dp[2] = [1, 1]
dp[3] = [2, 2]

for i in range(4, MAX+1):
    dp[i] = [(a+b+c) % MOD for a, b, c in zip(dp[i-1], dp[i-2], dp[i-3])]
    dp[i].reverse()

for i in n:
    print(" ".join(map(str, dp[i])))

"""
MAX x 2 보다 2 x MAX가 좀 더 빠를듯?
dp = [[0] * 100001 for _ in range(2)]
dp[0][1] = 1
dp[0][2], dp[1][2] = 1, 1
dp[0][3], dp[1][3] = 2, 2

for i in range(4, 100001):
    dp[0][i] = (dp[1][i - 1] + dp[1][i - 2] + dp[1][i - 3]) % MOD
    dp[1][i] = (dp[0][i - 1] + dp[0][i - 2] + dp[0][i - 3]) % MOD

for _ in range(int(input())):
    n = int(input())
    print(dp[0][n], dp[1][n])
"""