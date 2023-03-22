# 16195 1, 2, 3 더하기 9
"""
아이디어 : 15992를 그대로 사용하고 슬라이싱해서 합 구함
인덱스와 수를 맞춤. n을 만들기 위해 사용한 수의 갯수는 n-1, n-2, n-3의 각각의 방법에서 하나씩 늘린것.
[0]을 앞에 붙여주는 것을 잘 봐야된다.
"""
import sys
input = sys.stdin.readline
MOD = 10**9 + 9
T = int(input())

dp = [[0] * 1001 for i in range(1001)]
dp[1][0] = 1
dp[2][0], dp[2][1] = 1, 1
dp[3][0], dp[3][1], dp[3][2] = 1, 2, 1

for i in range(4, 1001):
    dp[i] = [0] + [(a+b+c) % MOD for a, b, c in zip(dp[i-1], dp[i-2], dp[i-3])]

for _ in range(T):
    n, m = map(int, input().split())
    print(sum(dp[n][:m]) % MOD)

"""
from itertools import *

s = [0, [1], [1, 1], [1, 2, 1]]
d = 1000000009

for i in range(4, 1001):
    s.append([0] + [*map(lambda x: sum(x) % d, [*zip_longest(*s[-3:], fillvalue=0)])])

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(sum(s[n][:m]) % d)
"""