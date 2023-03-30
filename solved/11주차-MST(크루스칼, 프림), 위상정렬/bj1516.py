# 1516 게임 개발
"""
    각각의 건물이 동시에 지어질 수 있으므로, 조건이 충족되자마자 건설을 시작한다.
    결국 동적계획법처럼 풀었다.
    위상정렬을 이용해 풀어볼 것
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