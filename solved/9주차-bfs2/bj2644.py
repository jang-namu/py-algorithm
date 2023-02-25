# 2644 촌수계산
"""
    부모 - 자식간의 관계는 그래프에서 edge(간선)를 나타낸다.
    그래프를 구성하고, 이를 탐색해서 노드간의 거리를 구한다.
"""
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
s, e = map(int, input().split())
M = int(input())

adj = [[] for _ in range(N+1)]
for _ in range(M):
    parent, child = map(int, input().split())
    adj[parent].append(child)
    adj[child].append(parent)


def dfs(s, e):
    queue = deque()
    queue.append(s)
    visited = [0] * (N + 1)

    while queue:
        now = queue.popleft()

        for next in adj[now]:
            if visited[next] == 0:
                visited[next] = visited[now] + 1
                queue.append(next)
            if next == e:
                return visited[next]
    return -1


print(dfs(s, e))