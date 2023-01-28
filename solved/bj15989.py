# 15989 1, 2, 3 더하기 4
import sys
input = sys.stdin.readline


def getNum(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if n-3 >= 0:
        tmp = getNum(n-3)

dp = [0] * 11
T = int(input())
for _ in range(T):
    n = int(input())
    getNum(n)
    print(dp)