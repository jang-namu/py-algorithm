# 1445 일요일 아침의 데이트
"""
    백준 풀이 참고한 코드.
    가중치를 저장하는 배열을 따로 만들 필요 없이 우선순위 큐에 같이 묶어서 넣는다.
    visited를 작성할 필요가 없고, 쓸데없이 무거운 adj를 만드는 것도 다익스트라 내부에서 if문을 사용하여 처리했다.
"""
import sys
from heapq import heappush, heappop
input = sys.stdin.readline


def dijkstra(start_y, start_x):
    pq = [(0, start_y, start_x)]  # g = 5000, g_side = 1
    processed = [[False] * M for _ in range(N)]
    while pq:
        g, y, x = heappop(pq)
        if forest[y][x] == 'F':
            return g
        if processed[y][x]:
            continue
        processed[y][x] = True
        for dy, dx in Deltas:
            if 0 <= (ny := y + dy) < N and 0 <= (nx := x + dx) < M:
                if forest[ny][nx] == 'g':
                    heappush(pq, (g+5000, ny, nx))
                elif forest[ny][nx] == '.':
                    is_g_side = False
                    for ey, ex in Deltas:
                        if 0 <= (sy := ny + ey) < N and 0 <= (sx := nx + ex) < M:
                            if forest[sy][sx] == 'g':
                                is_g_side = True
                                break
                    heappush(pq, (g + is_g_side, ny, nx))
                else:
                    heappush(pq, (g, ny, nx))


Deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
N, M = map(int, input().split())
forest = [input().rstrip() for _ in range(N)]
for i in range(N):
    for j in range(M):
        if forest[i][j] == 'S':
            start_y, start_x = i, j
            ans = dijkstra(start_y, start_x)
            print(ans // 5000, ans % 5000)
            exit(0)


"""
    사실 어려울건 없는 문제였다. TC를 몇 개 만들어 넣는 것 만으로 문제가 보였다.
    ex 1)  3 3              ex2) 3 3
           ggS                   ggS
           ggg                   gFg
           Fgg                   ggg
    1번, 입력받는 과정에서 g를 만났을 때 if adj[ny][nx] == 0:를 조건을 추가하지 않으면 g근처 g도 1로 초기화된다.
    2번, 힙에서 뺄 때 검사하게되면 F가 g근처에 있을 때, F도 포함해서 세어버린다.

    TC를 잘 작성하자. 특히나 예제 TC가 많이 주어지지 않을 때.

    알고리즘 적으로는 기존 bfs 동서남북 이동 문제에 다익스트라를 도입했다.
    즉, 우선순위(쓰레기 가중치)를 기준으로 쓰레기, 쓰레기 주변을 덜 지나간 것부터 빼낸다.

    이렇게만 하면 시간초과가 나기 때문에, 시간을 줄이기 위해서는 다익스트라의, processed까지 도입한다.
    즉, 다익스트라 알고리즘의 핵심. "한 번 검사된 노드에 대해서는 더 이상 시간이 줄어들지 않는다"는 점을 이용한다.
"""
"""
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

Deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
N, M = map(int, input().split())

adj = [[0] * (M+1) for _ in range(N+1)] # 각 칸에 쓰레기 = 5000, 쓰레기 인접 칸 = 1
for i in range(1, N+1):
    line = input().rstrip()
    for j in range(1, M+1):
        if line[j-1] == 'g':
            adj[i][j] = 5000
            for dy, dx in Deltas:
                if 0 < (ny := i + dy) <= N and 0 < (nx := j + dx) <= M:
                    if adj[ny][nx] == 0:    # 중요! g가 붙어있는 경우 뒤에 나오는 것 기준으로 1로 초기화될 수 있음
                        adj[ny][nx] = 1
        elif line[j-1] == 'S':
            start = (i, j)
        elif line[j-1] == 'F':
            end = (i, j)


def dijkstra(start, end):
    pq = []
    y, x = start
    end_y, end_x = end
    heappush(pq, (0, y, x))
    visited = [[1e10] * (M+1) for _ in range(N+1)]  # 해당 노드까지 가중치
    visited[y][x] = 0
    processed = [[False] * (M+1) for _ in range(N+1)]   # 작업 처리?, 처리한 노드는 더 이상 줄어들지 않음.

    while pq:
        w, y, x = heappop(pq)
        if processed[y][x]:
            continue
        processed[y][x] = True
        for dy, dx in Deltas:
            if 0 < (ny := y + dy) <= N and 0 < (nx := x + dx) <= M:
                if ny == end_y and nx == end_x: # 여기서 검사해야 F가 g근처일 때, 쓰레기 옆을 지나간 것이라고 안 셈.
                    return w
                visited[ny][nx] = w + adj[ny][nx]
                heappush(pq, (w+adj[ny][nx], ny, nx))
    return visited[end_y][end_x]


ans = dijkstra(start, end)
print(ans // 5000, ans % 5000)
"""