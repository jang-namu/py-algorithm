# https://school.programmers.co.kr/learn/courses/30/lessons/87377?language=python3

def solution(line):
    cross = set()

    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            x, y = calculate(line[i], line[j])
            if x == int(x) and y == int(y):  # 교점이 정수일때만(0.1인 경우 교점이 아닐 수 있음)
                cross.add((int(x), int(y)))

    x1 = max([e[0] for e in cross])
    x2 = min([e[0] for e in cross])
    y1 = max([e[1] for e in cross])
    y2 = min([e[1] for e in cross])

    answer = ["." * (abs(x1 - x2 + 1))] * abs(y1 - y2 + 1)

    color(answer, cross, x2, y1)
    return answer


# 교점 구하는 함수
def calculate(l1, l2):
    x = (l1[1] * l2[2] - l1[2] * l2[1]) / (l1[0] * l2[1] - l1[1] * l2[0]) if (l1[0] * l2[1] - l1[1] * l2[
        0]) != 0 else 0.1  # 교점이 없을 때, (정수가 아닌)아무런 소수 반환
    y = (l1[2] * l2[0] - l1[0] * l2[2]) / (l1[0] * l2[1] - l1[1] * l2[0]) if (l1[0] * l2[1] - l1[1] * l2[
        0]) != 0 else 0.1
    return (x, y)


def color(board, cross, min_x, max_y):
    for point in cross:
        r = max_y - point[1]
        c = point[0] - min_x
        board[r] = board[r][:c] + '*' + board[r][c + 1:]
