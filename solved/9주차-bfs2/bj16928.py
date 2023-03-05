# 16928 뱀과 사다리 게임
"""
    직선상에서 이뤄지는 그래프와 같다. 이동가능한 칸(move)을 range(1, 7)로 설정하고, 만들어지는 경우의 수를 검사한다.
    queue를 이용하여 최단 시간내에 100번재 칸에 도착하는 횟수를 찾으면 프로그램을 종료한다.

"""
# 아래 코드에서 불필요한 함수, 사전형 삭제 및 축약
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

ladder_snake = dict()
for _ in range(N + M):
    start, end = map(int, input().split())
    ladder_snake[start] = end

visited = [0] * 101


def bfs():
    queue = deque()
    queue.append(1)


    while queue:
        pos = queue.popleft()
        for dx in range(1, 7):
            npos = pos + dx
            if visited[npos]:
                continue
            if npos in ladder_snake:
                queue.append(ladder_snake[npos])
                visited[ladder_snake[npos]] = visited[pos] + 1
                continue
            if npos == 100:
                return visited[pos] + 1
            if npos > 100:
                continue
            queue.append(npos)
            visited[npos] = visited[pos] + 1


print(bfs())
for i in range(10):
    print(visited[i*10+1: i*10+111])

"""
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

ladder = dict()
for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y

snake = dict()
for _ in range(M):
    u, v = map(int, input().split())
    snake[u] = v


def is_ladder(pos):
    return ladder.get(pos) is not None


def is_snake(pos):
    return snake.get(pos) is not None


def bfs():
    queue = deque()
    queue.append(1)
    visited = [0] * 101

    count = 0
    while queue:
        print(queue)
        count += 1

        length = len(queue)
        for _ in range(length):
            pos = queue.popleft()
            for dx in range(1, 7):
                npos = pos + dx
                if visited[npos]:
                    continue
                if is_snake(npos):
                    queue.append(snake[npos])
                    visited[snake[npos]] = 1
                    continue
                if is_ladder(npos):
                    queue.append(ladder[npos])
                    visited[ladder[npos]] = 1
                    continue
                if npos == 100:
                    return count
                if npos > 100:
                    continue
                queue.append(npos)
                visited[npos] = 1


print(bfs())
"""