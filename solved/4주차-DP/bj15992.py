# 15992 1, 2, 3 더하기 7
"""
아이디어 : 1부터 6정도까지 경우의 수를 써보면 쉽게 이해가능.
결국 현재 수는, 이전 수에서 하나의 수를 더한 경우다.
즉, n은 n-1에서 1이라는 하나의 숫자를 더한것이고, n-2에서 하나의 숫자를 더 쓰고, 마찬가지로 n-3에서 3이라는 숫자를
하나 더 쓴 것이다.
따라서, n-1, n-2, n-3에서 하나씩 숫자를 더 쓴것으로 본다.
이걸 이해하면 15990과 비슷하게 풀 수 있다. 대신 이번엔 사용한 숫자의 갯수를 저장한다.
"""
import sys
input = sys.stdin.readline
MOD = 1000000009
T = int(input())
# 0부터 999까지 => 1부터 1000까지를 의미한다.
dp = list([0] * 1000 for _ in range(1000))
dp[0][0] = 1
dp[1][0], dp[1][1] = 1, 1
dp[2][0], dp[2][1], dp[2][2] = 1, 2, 1

for i in range(3, 1000):
    dp[i] = [0] + list((a+b+c) % MOD for a, b, c in zip(dp[i - 3], dp[i - 2], dp[i - 1]))

for _ in range(T):
    n, m = map(int, input().split())
    print(dp[n-1][m-1])

"""
for i in range(4, 1001):
    for j in range(1, i + 1):
        dp[i][j] = (dp[i - 1][j - 1] + dp[i - 2][j - 1] + dp[i - 3][j - 1]) % MOD

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(dp[a][b])
"""