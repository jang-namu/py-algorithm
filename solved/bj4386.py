# 4386 별자리 만들기
"""
크루스칼 알고리즘: 가중치를 기준으로 오름차순 정렬. 가중치가 작은 간선부터 추가해간다.
"""
import math
import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input())

vertex = [i for i in range(n + 1)]
size = [1] * (n + 1)

edges = []
stars = []
for _ in range(n):
    stars.append(list(map(float, input().split())))

for i in range(n):
    for j in range(i + 1, n):
        w = math.sqrt((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2)
        heappush(edges, (w, i, j))


def find(a):
    if a == vertex[a]:
        return a
    vertex[a] = find(vertex[a])
    return vertex[a]

def unite(a, b):
    a = find(a)
    b = find(b)
    if size[a] < size[b]:
        a, b = b, a
    size[a] += size[b]
    vertex[b] = a

weight = 0;
while edges:
    w, i, j = heappop(edges)
    if find(i) == find(j):
        continue
    unite(i, j)
    weight += w

print(round(weight, 2))

