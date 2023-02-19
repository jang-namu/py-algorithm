# 1260 DFS와 BFS
"""
    DFS(깊이 우선 탐색)는 최대한 깊이깊이 들어가서 끝에 다다르면 뒤로 돌아간 후 또 최대한 깊이깊이 들어감
    BFS(너비 우선 탐색)은 현재로부터 가까운것들 -> 먼것 순으로 모든 노드를 탐색
    파이썬에서 제공하는 Queue 클래스는 리스트로 구현, 굉장히 느림. => deque 사용(연결 리스트로 구현되어 있음) 빠르다.
    DFS, BFS에서 둘 다 중요한 점은 이미 갔던 노드를 체크하는 것.
    추가로 DFS는 재귀를 이용하면 쉽고, BFS는 반복문을 이용하면서, 큐를 이용해 거리 순으로 원소(노드)를 저장한다.
"""

import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

for i in range(N+1):
    adj[i].sort()

visited = [False] * (N+1)


def dfs(s):
    if visited[s]:
        return
    visited[s] = True
    print(s, end=" ")
    for v in adj[s]:
        dfs(v)


def bfs(V):
    q = deque()
    visited = [False] * (N+1)

    q.append(V)
    visited[V] = True
    while len(q) > 0:
        s = q.popleft()
        print(s, end=" ")
        for v in adj[s]:
            if visited[v]:
                continue
            visited[v] = True
            q.append(v)


dfs(V)
print()
bfs(V)

