# 16940 BFS 스페셜 저지
"""
    백준 답, 아이디어 : 현재 검사 중인 노드와 연결된 모든 노드들은 queue에 추가되야 한다.
    user_answer은 부모노드를 기준으로 나눌 수 있다. 이를 블록이라 하면.
    즉, 현재 검사 중인 노드(부모노드)와 연결된 모든 노드들은(visited가 False인) 순서는 달라질 수 있지만,
    다른 블록과는 순서가 뒤섞일 수 없다.
    set()은 순서가 없는 자료형으로, 이를 이용하면, 현재 검사중인 노드의 자식노드와 유저입력(슬라이싱한 부분)을 비교할 수 있다.

"""
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

user_answer = list(map(int, input().split()))
visited = [False] * (N+1)
visited[1] = True


def bfs():
    if user_answer[0] != 1:
        return 0

    queue = deque()
    queue.append(1)
    idx = 1
    while queue:
        cur = queue.popleft()
        children = []   # 현재 노드의 자식노드
        for child in adj[cur]:
            if not visited[child]:
                visited[child] = True
                children.append(child)

        l = len(children)
        cur_answer = user_answer[idx:idx + l]   # 유저 입력, 이번 노드의 자식 노드 순서
        if set(children) == set(cur_answer):    # 순서가 없는 set
            queue.extend(cur_answer)    # 유저 입력과 동일한 순서로 queue에 넣어준다.
            idx += l
        else:
            return 0
    return 1

print(bfs())



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