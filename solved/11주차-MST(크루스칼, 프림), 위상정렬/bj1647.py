# 1647 도시 분할 계획
"""
    마을을 두 개로 쪼개고, 그 와중에 양 마을에 MST 합이 최소가 되야 한다.

    문제를 분해한다.
    => 전체에 대한 MST를 구하면, MST는 트리이므로 간선을 하나 삭제 시, 두 개의 컴포넌트로 나뉜다.
    즉, 이 문제는 전체에 대해 MST를 한 번 구하고 구한 트리 중 가장 가중치가 높은 간선을 제거한다.
"""
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b, w = map(int, input().split())
    heappush(edges, (w, a, b))
link = [*range(N+1)]
size = [1] * (N+1)


def find(x):
    if x == link[x]:
        return x
    link[x] = find(link[x])
    return link[x]


def same(a, b):
    return find(a) == find(b)


def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

def unite(a, b):
    a = find(a)
    b = find(b)
    if size[a] < size[b]:
        a, b = swap(a, b)
    size[a] += size[b]
    link[b] = a


weight = []
while edges:
    w, a, b = heappop(edges)
    if not same(a, b):
        unite(a, b)
        weight.append(w)
print(sum(weight) - max(weight))