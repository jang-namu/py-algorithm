# 1922 네트워크 연결
"""
    해당 문제는 모든 정점을 잇는 subgrpah 중 간선의 가중치가 최소인 그래프를 찾는다.
    즉, MST 최소 스패닝 트리를 찾는 문제이다.
    크루스칼 알고리즘을 이용. 유니온-파인드를 통해 구현하였다.
"""
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
M = int(input())
edges = []
link = [*range(N+1)]
size = [1] * (N+1)
for _ in range(M):
    a, b, w = map(int, input().split())
    heappush(edges, (w, a, b))


def find(x):
    if x == link[x]:
        return x
    link[x] = find(link[x])
    return link[x]


def same(a, b):
    return find(a) == find(b)


def unite(a, b):
    a = find(a)
    b = find(b)
    if size[a] < size[b]:
        temp = a
        a = b
        b = temp
    size[a] += size[b]
    link[b] = a


weight = 0
while max(size) != N:
    w, a, b = heappop(edges)
    if not same(a, b):
        unite(a, b)
        weight += w

print(weight)