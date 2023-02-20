# 7576 토마토
"""
    아이디어 : 탐색을 하면서 상하좌우 한번씩만 익은 토마토로 만든다.
            for문을 사용하면 유기농 배추 문제와 같이, 순서에 따라 영향을 받기 때문에 for문은 사용할 수 없다.
            따라서, 현재 턴에서 익은 토마토를 저장해뒀다가 해당 토마토에 상하좌우에만 영향을 끼치도록 해야한다.
            또한, 매 iteration마다 tomato배열의 모든 원소에 대해 1인지 검사하는 것 보다.
            이전 iteration에서 새로 1이 된 토마토를 저장해서 사용하는 것이 훨씬 빠르다 (deque 이용)
            이렇게 될 경우 추가로 iteration 실행 시, 변화가 없을 때 종료조건도 넣지 않아도 된다.

    주의할 점 : 격자가 나오면, 항상 상하좌우에 '-1' 등의 숫자로 인덱스를 맞춰서 풀면 편리하다.
                하지만, 이 경우 꼭 !!이하 모든 코드에서 인덱스를 수정해야 한다.!!
"""
import sys
from collections import deque
input = sys.stdin.readline

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

M, N = map(int, input().split())
tomato = [[-1] * (M+2)]
tomato += list([-1] + list(map(int, input().split())) + [-1] for _ in range(N))
tomato += [[-1] * (M+2)]


def bfs():
    length = len(jmt)
    for _ in range(length):
        row, column = jmt.popleft()
        for x, y in move:
            nr = row + y
            nc = column + x
            if tomato[nr][nc] == 0:
                tomato[nr][nc] = 1
                jmt.append((nr, nc))


def check_tomato():
    for i in range(1, N+1):     # 1번부터 시작하는 인덱스에 유의!
        for j in range(1, M+1):
            if tomato[i][j] == 0:
                return False
    return True


jmt = deque()
for row in range(1, N+1):
    for column in range(1, M+1):
        if tomato[row][column] == 1:
            jmt.append((row, column))

for count in range(N * M):
    if jmt:
        bfs()
    else:
        break

print(count-1 if check_tomato() else -1)


"""
# check_tomato() 함수 필요없이, 처음에 안 익은 토마토 갯수를 세서, 익을 때마다 숫자를 줄여나감
ans = -1
cnt = 0

for i in range(1, N + 1):
	for j in range(1, M + 1):
		if arr[i][j] == 0:
			cnt += 1
		elif arr[i][j] == 1:
			q.append((i, j))

while q:
	new_q = []
	for i, j in q:
		for dy, dx in d:
			y, x = i + dy, j + dx
			if arr[y][x] == 0:
				cnt -= 1
				arr[y][x] = 1
				new_q.append((y, x))
	q = new_q
	ans += 1        # 무한 for문 대신 queue가 빌때까지.

print(ans if cnt == 0 else -1)
"""