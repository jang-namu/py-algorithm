# 1516 게임 개발
"""
    위상정렬 구현, 진입차수(in_degree) 배열을 만들고, in_degree가 0이 되면 조건 충족했다고 보고
    건설을 시작한다.

"""
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
build = [[]]
condition = [[] for _ in range(N+1)]
in_degree = [[]]
for i in range(1, N+1):
    time, *cond, _ = map(int, input().split())
    in_degree.append(len(cond))
    build.append((time, cond))
    for j in cond:
        condition[j].append(i)


def topological_sort():
    ans = [0] * (N+1)
    q = deque()
    for i in range(1, N+1):
        if in_degree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        ans[now] = max(ans[k] for k in build[now][1]) if build[now][1] else 0
        ans[now] += build[now][0]
        for i in condition[now]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                q.append(i)
    return ans


ans = topological_sort()
print('\n'.join(map(str, ans[1:])))





"""
    각각의 건물이 동시에 지어질 수 있으므로, 조건이 충족되자마자 건설을 시작한다.
    결국 동적계획법처럼 풀었다.
    위상정렬을 이용해 풀어볼 것
"""
"""
import sys
input = sys.stdin.readline

N = int(input())
time = []
demand = []
for _ in range(N):
    t, *arr = map(int, input().split())
    time.append(t)
    demand.append(arr[:-1])

visited = [False] * N
ans = [1e10] * N
while True:
    for i in range(N):
        sign = True
        for k in demand[i]:
            if not visited[k-1]:
                sign = False
                break
        if sign:
            visited[i] = True
            ans[i] = time[i]
            if demand[i]:
                ans[i] += max(ans[k-1] for k in demand[i])
    if sum(visited) == N:
        break
print('\n'.join(map(str, ans)))
"""