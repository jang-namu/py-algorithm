# 16940 BFS 스페셜 저지
"""
    너무 느리다.
    설명 : 처음 시작 노드는 1로 고정이다. 연결된 노드의 탐색 순서는 랜덤이지만,
    먼저 탐색한 노드의 자식노드가 먼저 나와야한다.
    1
    2       3
    4 5     6 7 일 때,
    1 -> 3 -> 2 -> 6 -> 7 -> 5 -> 4는 가능하지만
    1 -> 3 -> 2 _> 4 -> 5 -> 6 -> 7은 불가능하다.
"""
"""
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
adj = list([] for _ in range(N + 1))
for _ in range(N-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

verify = deque(list(map(int, input().split())))

pos = 1     # 시작노드는 1로 고정
check = verify.popleft()
if pos != check:    # 처음부터 다르면 종료
    print(0)
    exit(0)

queue = deque()

while adj[pos]:     # pos는 현재 검사하고 있는 부모 노드. pos의 자식 노드를 모두 검사하고 다음으로 넘어간다.
    child = verify.popleft()
    if child in adj[pos]:   # 있으면, 양쪽에서 삭제. queue에는 추후 parent가 될 child를 넣는다.
        adj[pos].remove(child)
        adj[child].remove(pos)
        queue.append(child)
    else:
        print(0)
        exit(0)
    if not adj[pos]:    # 현재 검사중인 pos(부모 노드)의 간선 정보가 비면, queue에서 다음 노드를 꺼낸다.
        pos = queue.popleft()
print(1)
"""