# 2887 행성 터널
"""
    코멘트: 쫄지마!

    두 행성 간 터널 건설 비용이 min(abs(x-x)+abs(y-y)+abs(z-z))가 아닌,!!
    min(abs(x-x), abs(y-y), abs(z-z))임에 주의하라!
    후자의 경우, 계산이 훨씬 간단해진다.

    읽어보면 확실하게 MST를 구해야 하는 문제임을 쉽게 알아차릴 수 있다.
    문제는 간선의 전처리를 어떻게하냐.
    단순하게 생각해서 x, y, z 각 좌표를 sort()하면, i번쨰와 i-1번째의 차이가 가장 작을 것이다.

"""
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
xpos = []
ypos = []
zpos = []
for i in range(N):
    x, y, z = map(int, input().split())
    xpos.append((x, i))
    ypos.append((y, i))
    zpos.append((z, i))
xpos.sort()
ypos.sort()
zpos.sort()

heap = []
for i in range(N-1):
    heappush(heap, (abs(xpos[i][0] - xpos[i + 1][0]), xpos[i][1], xpos[i + 1][1]))
    heappush(heap, (abs(ypos[i][0] - ypos[i + 1][0]), ypos[i][1], ypos[i + 1][1]))
    heappush(heap, (abs(zpos[i][0] - zpos[i + 1][0]), zpos[i][1], zpos[i + 1][1]))

size = [1] * (N+1)
link = [*range(N+1)]


def find(x):
    if x == link[x]:
        return x
    link[x] = find(link[x])
    return link[x]


def same(a, b):
    return find(a) == find(b)


def swap(a, b):
    tmp = b
    b = a
    a = tmp
    return a, b


def unite(planet1, planet2):
    a = find(planet1)
    b = find(planet2)
    if size[a] < size[b]:
        a, b = swap(a, b)
    size[a] += size[b]
    link[b] = a


time = 0
weight = 0
while time != N-1:
    w, a, b = heappop(heap)
    if not same(a, b):
        unite(a, b)
        time += 1
        weight += w
print(weight)
