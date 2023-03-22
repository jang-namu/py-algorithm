# 2178 미로 탐색
"""
# 미로 탐색에서 최단거리를 찾을 때, 스택을 사용하면 안 되는 이유
# => 스택을 사용하게 될 경우, 가장 마지막에 추가한 원소를 빼내게 된다. 즉, 목적지에 도달하는것 만을 생각한다.
# 따라서, move의 방향에 따란 목적지까지의 경로가 여러가지 경우가 생길 수 있다.
# 큐를 사용하게 되면, 같은 iter에 경로에서 최단경로를 선택해 나아간다.

def bfs():
    table[0][0]=-1
    que=[(0,0)]
    while que:
        ci, cj=que.pop(0)   # pop() '0'에 주의 => queue와 같은 역할을 한다.
        for di,dj in [(-1,0), (0,1), (1,0), (0,-1)]:
            ni = ci + di
            nj = cj + dj
            if 0<= ni < n and 0<= nj<m and table[ni][nj]==1:    # 같은 칸은 한번만 밟는다. => because, queue이기 때문에
                table[ni][nj] = table[ci][cj] - 1               # !!!더 짧은 경로가 먼저 나온다.!!!
                que.append((ni,nj))
            if ni==n-1 and nj==m-1: return



n,m = map(int, input().split())
table=[]
for _ in range(n):
    table.append([int(x) for x in list(input().strip())])
bfs()
print(-table[n-1][m-1])





"""
"""
    아이디어 : 시간초과를 해결하기 위해 재귀가 아닌 queue를 이용한 반복으로 해결했다.
    같은 칸에 대해 ditance가 더 작은 결과가 나오면 queue에 새로 추가한다.
"""
import sys
from collections import deque
input = sys.stdin.readline

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, M = map(int, input().split())
maze = list(list(int(x) for x in input().rstrip()) for _ in range(N))
distance = [[10001] * M for _ in range(N)]


def bfs(row, column):
    queue = deque()
    queue.append((row, column))
    distance[0][0] = 1


    while queue:
        row, column = queue.popleft()
        for dy, dx in move:
            ny = row + dy
            nx = column + dx
            if nx >= 0 and nx < M and ny >=0 and ny < N:
                if maze[ny][nx] and distance[ny][nx] > distance[row][column] + 1:
                    distance[ny][nx] = distance[row][column] + 1
                    queue.append((ny, nx))
                if ny == N-1 and nx == M -1:
                    return


bfs(0, 0)
print(distance[-1][-1])


"""
# 시간초과 재귀함수 내부에서, 모든 경우에 비교를 해야하므로 굉장히 느린것으로 보임.
# visited와 maze를 합칠 순 없을까. 어차피, maze의 갈 수 있는 칸은 1이상이기만 하면된다.
# 이미 한 번간 경로를 다시 돌아가는 경우를 어떻게 제외할 수 있을까
# => 처음 방시대로 큐에 저장한다. 문제는 어떻게 방문 상태를 특정 시점을 기준으로 되돌릴 것이냐.
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, M = map(int, input().split())
maze = list(list(int(x) for x in input().rstrip()) for _ in range(N))

path = N * M
visited = list([10001] * M for _ in range(N))
visited[0][0] = 1


def bfs(row, column):
    global path
    if row == (N - 1) and column == (M - 1):
        path = min(path, visited[row][column])
        return

    for dx, dy in move:
        nx = column + dx
        ny = row + dy

        if 0 <= nx < M and 0 <= ny < N and maze[ny][nx]:
            if visited[ny][nx] > visited[row][column] + 1:
                visited[ny][nx] = visited[row][column] + 1
                dfs(ny, nx)


dfs(0, 0)
print(path)
"""
