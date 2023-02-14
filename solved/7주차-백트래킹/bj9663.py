# 9663 N-Queen
""" # 현재 속도가 너무 느리다.
매개변수 put은 column과 동시에 놓은 퀸의 갯수를 의미한다.
또한, 퀸은 왼쪽에서 오른쪽으로 한 칸씩 이동하면서밖에 놓지 못 한다고 제한.
퀸을 어떤 행에 놓을지만을 결정하면 된다.
또한, 이전에 선택된 행은 선택하지 못하기에 row_check 리스트를 두어 관리.
check함수는 퀸이 공격하는 대각을 표시.
uncheck는 재귀함수가 종료되고 돌아오면, 앞서 check한 위치를 다시 되돌린다.


다른 방법 : 각 행만을 선택할 때, 1차원 리스트를 두어 관리하는 방법.
이렇게 될 경우 재귀호출이 끝나고 돌아와 복구하기 위해, 변경 전 리스트를 따로 저장해야할 것으로 예상
다만 이와같은 방식으론 재귀가 깊어짐에따라 메모리 사용이 누적된다.
"""
N = int(input())

board = [[0] * N for _ in range(N)]
move = [(1, 1), (-1, 1)]
row_check = [0] * N
res = 0


def check(r, c):
    for x, y in move:
        dr = r
        dc = c
        while dr >= 0 and dr < N and dc < N:
            board[dr][dc] += 1
            dr += x
            dc += y


def uncheck(r, c):
    for x, y in move:
        dr = r
        dc = c
        while dr >= 0 and dr < N and dc < N:
            board[dr][dc] -= 1
            dr += x
            dc += y


def get_N_Queen(put=0):
    if put == N:
        global res
        res += 1
        return

    for i in range(N):
        if board[i][put] or row_check[i]:
            continue

        check(i, put)
        #print("깊이 :", res, "r :", i, "c :", put)
        row_check[i] += 1
        get_N_Queen(put+1)
        uncheck(i, put)
        row_check[i] -= 1


get_N_Queen()
print(res)



"""
    선택할 때 선택하지 못할 칸은 표시하는게 아니라, 선택한 해당 칸만 표시하고
    이후 iter에서 각 칸을 검사(왼쪽 대각 위,아래로 올라가며 표시된 칸이 있는지)
    but 이 방법은 각 칸마다 모두 검사하므로 위에 방법보다 비효율적.
"""
"""
N = int(input())

board = [[0] * N for _ in range(N)]
move = [(-1, -1), (1, -1)]
check = [0] * N
res = 0


def comp(r, c):
    for x, y in move:
        dr = r + x
        dc = c + y
        while 0 <= dr < N and 0 <= dc:
            if board[dr][dc]:
                return False
            dr += x
            dc += y
    return True


def get_N_Queen(pre=-5, put=0):
    if put == N:
        global res
        res += 1
        return

    for i in range(N):
        if check[i] or abs(i-pre) == 1:
            continue

        if comp(i, put):
            #print("깊이 :", res, "r :", i, "c :", put)
            board[i][put] = 1
            check[i] = 1
            get_N_Queen(i, put+1)
            board[i][put] = 0
            check[i] = 0


get_N_Queen()
print(res)
"""