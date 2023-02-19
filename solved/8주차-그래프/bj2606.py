# 2606 바이러스
"""
    아이디어 : 단순히 노드 1에서 시작하는 bfs, 또는 dfs로 탐색되는 노드의 갯수를 세면된다.
"""

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

visited = [False] * (N+1)


def dfs(s):
    if visited[s]:
        return
    visited[s] = True
    for x in graph[s]:  # 위에 if문을 for문안에 넣으면 더 빠르다.
        dfs(x)


dfs(1)
print(sum(visited) - 1) # sexy point. ^^7 'True == 1'
