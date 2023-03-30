# 1197 최소 스패닝 트리
"""
    MST는 구현 시, 유니온-파인드 자료구조를 사용한다.
    유니온-파인드 자료구조는 집합의 묶음을 관리하는 구조로, 두 집합을 합치는 unite와
    주어진 원소가 포함된 집합의 대표값을 구하는 find 연산이 있다.

    즉, 대표값을 비교하여 두 원소가 같은 집합에 있는지 아닌지 확인하기 위한 자료구조이다.

    구현 시 주의할 점은 unite등에서 대표값을 가리키는 배열(vertex)의 내용을 update할 때,
    그전에 반드시 find로 대표값을 찾은 후 비교 및 업데이트 한다.
"""
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

V, E = map(int, input().split())
vertex = [i for i in range(V+1)]
size = [1] * (V+1)
edges = []
for _ in range(E):
    a, b, w = map(int, input().split())
    heappush(edges, (w, a, b))


def find(x):
    if x == vertex[x]:
        return x
    vertex[x] = find(vertex[x])
    return vertex[x]


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
    vertex[b] = a


ans = 0
for _ in range(E):
    w, a, b = heappop(edges)
    if same(a, b):
        continue
    unite(a, b)
    ans += w
print(ans)

