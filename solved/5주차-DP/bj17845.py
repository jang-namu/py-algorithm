# 17845 수강 과목
"""
아이디어 : 16493 최대 페이지수 문제와 같다.
dp의 인덱스는 공부할 수 있는 시간을 나타내고, 해당 시간에 최대 중요도를 나타낸다.
1차원 배열로 문제를 해결할 경우, 뒤에부터 계산을 시작해야 같은 과목을 두번 이상 공부하지 않는다.
"""
"""
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
subject = list(tuple(map(int, input().split())) for _ in range(K))

dp = [0] * (N+1)
for value, time in subject:
    for i in range(N, time-1, -1):
        dp[i] = max(dp[i-time] + value, dp[i])
print(dp[-1])
"""

"""
2차원 배열로 풀이. 각 subject마다 행을 만들고, 1"""
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
subject = list(tuple(map(int, input().split())) for _ in range(K))

dp = [[0] * (N+1) for _ in range(K+1)]
for i in range(1, K+1):
    value, time = subject[i-1][0], subject[i-1][1]
    for j in range(1, N+1):
        if j - time >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-time] + value)
        else:
            dp[i][j] = dp[i-1][j]
print(dp)
print(dp[-1][-1])
