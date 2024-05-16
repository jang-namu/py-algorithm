# 골드 4

# 뱀은 처음에 1,1 오른쪽을 향한다.
# 몸을 늘려 머리를 다음칸에 위치시킴 (벽이나 자기자신의 몸과 부딪히면 끝난다)
# 이동한 칸에 있으면 사과는 없어지고 꼬리는 움직이지 않는다. (사과를 먹으면 길이가 늘어난다.)
# 사과가 없으면 몸길이를 줄여 꼬리가 위치한 칸을 비워준다.

# 뱀이 마지막에 꼬리가 있는 칸으로 머리를 움직이면 게임이 종료되어야 한다.

# 사과 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산해라.
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]
L = int(input())

# X초가 끝난 뒤 방향 회전
# L = 왼쪽 90도, D = 오른쪽 90도
heads = [list(input().split()) for _ in range(L)]
heads = deque(heads)
for head in heads:
    head[0] = int(head[0])

# 시작부터 시계방향
HEAD = [[0, 1], [1, 0], [0, -1], [-1, 0]]
head_idx = 0

snake = deque()
snake.append([1, 1])


def wall(size, row, col):
    if row < 1 or row > size or col < 1 or col > size:
        return True
    return False


def body(snake, row, col):
    for r, c in snake:
        if r == row and c == col:
            return True
    return False


def apple(apples, snake, row, col):
    for r, c in apples:
        if r == row and c == col:
            apples.remove([r, c])
            return
    snake.popleft()


def handle(heads, stage):
    if heads[0][0] != stage:
        return head_idx
    x, c = heads.popleft()
    if c == 'L':
        return (head_idx - 1 + 4) % 4
    return (head_idx + 1) % 4


for stage in range(1, N**2 + 1):
    row = snake[-1][0] + HEAD[head_idx][0]
    col = snake[-1][1] + HEAD[head_idx][1]
    if body(snake, row, col):
        print(stage)
        break
    if wall(N, row, col):
        print(stage)
        break

    snake.append([row, col])
    apple(apples, snake, row, col)

    if heads:
        head_idx = handle(heads, stage)

