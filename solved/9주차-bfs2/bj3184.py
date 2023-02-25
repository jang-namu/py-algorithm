# 3184 양
"""
    컴포넌트 별로 탐색, 탐색과정에서 양과 늑대의 수를 세고, 빈공간은 다음 탐색을 위해서 queue에 추가
    울타리는 그냥 넘긴다.
    visited를 통해 방문한 노드를 관리하고 모든 노드를 단 한번씩만 방문하도록 설계했다.
    간단하게 전역변수를 선언해 최종 생존한 양과 늑대수를 구했다.
"""
import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())

yard = [[char for char in input().rstrip()] for _ in range(r)]
visited = [[False] * c for _ in range(r)]
sheep = 0
wolf = 0


def bfs(row, column):
    global wolf, sheep
    queue = deque()
    queue.append((row, column))
    visited[row][column] = True

    t_sheep = 0
    t_wolf = 0

    while queue:
        row, column = queue.popleft()
        if yard[row][column] == 'v':
            t_wolf += 1
        elif yard[row][column] == 'o':
            t_sheep += 1
        for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
            nx = column + dx
            ny = row + dy
            if 0 <= nx < c and 0 <= ny < r and not visited[ny][nx]:
                visited[ny][nx] = True
                if yard[ny][nx] == '#':
                    continue
                queue.append((ny, nx))

    if t_wolf >= t_sheep:
        wolf += t_wolf
    else:
        sheep += t_sheep



for i in range(r):
    for j in range(c):
        if not visited[i][j] and yard[i][j] != '#':
            bfs(i, j)

print(sheep, wolf)


"""
# 백준 풀이, 재귀를 이용한 방법. 비슷해서 함수만 가져왔다.
# sheep와 wolf는 외부에서 선언, 최종적으로 sheep_sum, wolf_sum에 더해 최종결과 구함

def dfs(a, b):
    global sheep
    global wolf
    if graph[a][b] == 'o':
        sheep += 1
    elif graph[a][b] == 'v':
        wolf += 1
    graph[a][b] = '#'
    if b-1 >= 0 and graph[a][b-1] != '#':
        dfs(a, b-1)
    if b+1 < c and graph[a][b+1] != '#':
        dfs(a, b+1)
    if a-1 >= 0 and graph[a-1][b] != '#':
        dfs(a-1, b)
    if a+1 < r and graph[a+1][b] != '#':
        dfs(a+1, b)
"""