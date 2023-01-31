# 11722 가장 긴 감소하는 부분 수열
"""
아이디어: 11053의 백준 풀이를 참고했다.
아무래도 모든상황에 2중 for문을 이용하는 것보단, 아래와 같이 분기를 나눠서
필요할때만 for문을 도는 것이 훨씬 빠르다.
dp에 마지막원소(현재 수열에서 가장 작은수) 보다 작은 수가 들어오면 추가하고
그보다 큰 수가 들어오면, dp 배열에서 알맞은 위치에 값과 바꾼다.
"""

import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
dp = [A[0]]

for i in range(1, n):
    if A[i] < dp[-1]:
        dp.append(A[i])
    else:
        for j in range(len(dp)):
            if dp[j] <= A[i]:       # "<="을 써야한다 '같다'가 안들어가면 틀림.
                dp[j] = A[i]        # 이미 dp에 있는 수가 들어오면 같은 위치에 대입하고 빨리 루프를 종료시켜야함
                break               # "<"를 쓰게되면 그보다 더 작은수가 바뀌어버림 ex [100, 90] => [100, 100]

        """ 같은 일을 수행하지만, enumerate를 이용하면 좀 더 효율적이고, 클린코딩할 수 있다.
        for j,v in enumerate(stack):
            if i >= v:
                stack[j] = i
                break
                """
