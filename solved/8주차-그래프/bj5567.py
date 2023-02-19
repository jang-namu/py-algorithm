# 5567 결혼식
"""
    아이디어 : bfs를 이용. 거리가 2 이상이면 더 이상 추가안하는 조건식을 달았다.
"""
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(s):
    count = -1
    queue = deque()
    visited = [False] * (n + 1)
    distance = [0] * (n+1)

    queue.append(s)
    visited[s] = True

    while len(queue):
        v = queue.popleft()
        count += 1
        if distance[v] >= 2:
            continue
        for x in graph[v]:
            if visited[x]:
                continue
            visited[x] = True
            distance[x] = distance[v] + 1
            queue.append(x)
    return count


print(bfs(1))


"""
# 이웃 노드의 이웃. 즉, 거리가 2 이내인 노드만을 탐색.
# frineds 1차 배열에 친구관계를 정리한다.
# 일차적으로 나와의 친구들을 저장하고, 친구들의 친구들을 저장한다.
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [[] for _ in range(n + 1)]
friends = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

if not arr[1]:
    print(0)
else:
    for i in arr[1]:
        friends[i] = 1
        for j in arr[i]:
            friends[j] = 1
    print(friends.count(1) - 1)

"""