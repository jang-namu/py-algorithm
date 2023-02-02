# 14002 가장 긴 증가하는 부분 수열 4
"""
# 치팅코드 : dp에 자기자신을 포함한 가장 긴 수열의 길이를 구한다
# 수열을 알기위해, dp의 뒤부터 검색을 시작해서, max(dp), max(dp-1), max(dp-2) 순으로 찾는다.
# 뒤부터 검색하는 이유 : 원래 배열에 요소들은 max(dp)보다 작다.
# 또한, max(dp)에 "왼쪽에 있어야한다."
import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))

dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if A[i] > A[j] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1

print(max(dp))
res = []
point = max(dp)
for i in range(n-1, -1, - 1):
    if dp[i] == point:
        res.append(A[i])
        point -= 1
res.reverse()
print(" ".join(map(str, res)))
"""

"""
# 내 풀이. 왜 안될까 
import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))

dp = [A[0]]
res = [A[0]]
for i in range(1, n):
    if A[i] > dp[-1]:
        dp.append(A[i])
        res.append(A[i])
    else:
        for j in range(len(dp)):
            if A[i] < dp[j]:
                dp[j] = A[i]
                if j == len(dp)-1:
                    res = [ele for ele in dp]
                break

print(len(dp))
#print(dp)
print(*res)
"""