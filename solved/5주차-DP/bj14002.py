# 14002 가장 긴 증가하는 부분 수열 4
import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))

dp = [A[0]]
res = []
for i in range(1, n):
    if A[i] > dp[-1]:
        dp.append(A[i])
        for j in range(len(res)):
            res[j].append(A[i])
    else:
        for j in range(len(dp)):
            if dp[j] > A[i]:
                res.append([ele for ele in dp])
                dp[j] = A[i]

print(dp)
print(res)