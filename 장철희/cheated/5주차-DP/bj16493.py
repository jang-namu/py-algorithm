# 16493 최대 페이지 수
"""
아이디어 : 짐을 하나씩 추가해 가면서 0~N일까지 최대 가치를 구한다.
            이차원 배열로 구현 시, k번째 짐을 쓰지 않고 N일을 만드는 것과
            k번째 짐을 쓰고 만드는 것을 max로 비교한다.
"""

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
book = list(tuple(map(int, input().split())) for _ in range(M))
print(book)

dp = [[0] * (N+1) for _ in range(M+1)]
for i in range(1, M+1):
    day, page = book[i-1][0], book[i-1][1]
    for j in range(1, N+1):
        if j - day >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-day] + page)
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1])

"""
# knapsack 문제는 뒤에서부터 연산하는 트릭을 사용해서 1차원으로 효율적 해결이 가능하다.
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
d = [0] * (N+1)
for _ in range(k):
    day, page= map(int, input().split())
    for i in range(N, day-1, -1):
        d[i] = max(d[i], d[i-day] + page)
print(d[n])
"""