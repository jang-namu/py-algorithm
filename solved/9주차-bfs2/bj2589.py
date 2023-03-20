import sys
from collections import deque
input = sys.stdin.readline

Deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
dic = {'W':0, 'L':1}
N, M = map(int, input().split())
world = [list(input().rstrip()) for i in range(N)]
print(world)
for temp in world:
    for j in range(M):
        temp[j] = dic[temp[j]]

def bfs(row, column):
    queue = deque()
    queue.append((row, column))
    visited = [[0] * M for _ in range(N)]
    visited[row][column] = True
    depth = -1
    while queue:
        depth += 1
        new_queue = deque()
        while queue:
            y, x = queue.popleft()
            for dy, dx in Deltas:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                    if world[ny][nx]:
                        visited[ny][nx] = True
                        new_queue.append((ny, nx))
        queue = new_queue
    return depth


ans = 0
for i in range(N):
    for j in range(M):
        # continue로 탈출하는 조건이 속도의 핵심(육지 세개가 붙어있으면, 가운데에서 시작해서는 절대로 최장경로가 안됨
        if 1 <= j < M-1 and world[i][j-1] and world[i][j+1]:
            continue
        elif 1 <= i < N-1 and world[i-1][j] and world[i+1][j]:
            continue
        elif world[i][j]:
            ans = max(ans, bfs(i, j))
print(ans)





"""
    단순히 bfs를 통해 최대 depth를 알아내는 문제.
    모든 육지를 한 번씩, 시작 노드로 하는 bfs를 돌도록 설계
    놓친 점 : 시작노드를 체크하지 않아 두번 틀림.
"""
"""
import sys
from collections import deque
input = sys.stdin.readline

Deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, M = map(int, input().split())
world = list(input().rstrip() for _ in range(N))


def bfs(row, column):
    queue = deque()
    queue.append((row, column))
    visited = [[0] * M for _ in range(N)]
    visited[row][column] = 1    # 시작노드 체크 중요!
    depth = -1
    while queue:
        depth += 1
        for _ in range(len(queue)):
            y, x = queue.popleft()
            for dy, dx in Deltas:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                    if world[ny][nx] == 'L':
                        visited[ny][nx] = 1
                        queue.append((ny, nx))
    return depth


res = 0
for i in range(N):
    for j in range(M):
        if world[i][j] == 'L':
            cur = bfs(i,j)
            if cur > res:
                res = cur
print(res)
"""


"""틀림"""
"""
def bfs(row, column):
    queue = deque()
    queue.append((row, column))

    depth = -1
    while queue:
        depth += 1
        for _ in range(len(queue)):
            y, x = queue.popleft()
            for dy, dx in Deltas:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                    if world[ny][nx] == 'L':
                        visited[ny][nx] = 1
                        queue.append((ny, nx))
    return depth


res = 0
for i in range(N):
    for j in range(M):
        visited = [[0] * M for _ in range(N)]
        if world[i][j] == 'L':
            res = max(bfs(i, j), res)
print(res)
"""
"""
1 2
LL

답 : 1
위에 로직에 넣으면 2가 나옴. 처음 시작노드를 visited에 표시하고 bfs를 사용해야 한다.
"""