# 1068 트리
"""
    2023.05.02
    트리를 그래프의 인접행렬로 만들어 해결했다.
    리프노드는 자신으로부터 그 자식으로 뻗어나가는 간선이 없다.
    문제에서 삭제된 노드를 루트로 하는 서브트리의 노드들은 루트로 가는 길을 끊어버리면 신경쓰지 않아도된다.
"""
import sys
input = sys.stdin.readline

n = int(input())
parent = list(map(int, input().split()))
removed = int(input())

graph = [[] for _ in range(n)]
stack = []
for i, node in enumerate(parent):
    if i == removed:
        continue
    elif node != -1:
        graph[node].append(i)
    else:
        stack.append(i)

count = 0
while stack:
    node = stack.pop()
    if not graph[node]:
        count += 1
    else:
        for next in graph[node]:
            stack.append(next)

print(count)

