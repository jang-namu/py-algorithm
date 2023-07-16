"""
    스터디 설명 들은 문제.
"""
import math


def cal_distance(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def solution(m, n, startX, startY, balls):
    answer = []

    for x, y in balls:
        minimum = -1
        if startX == x:
            if startY > y:
                minimum = min(cal_distance(startX, startY, -x, y),
                              cal_distance(startX, startY, 2 * m - x, y),
                              cal_distance(startX, startY, x, 2 * n - y))
            else:
                minimum = min(cal_distance(startX, startY, -x, y),
                              cal_distance(startX, startY, 2 * m - x, y),
                              cal_distance(startX, startY, x, -y))
        elif startY == y:
            # elif는 통과, if는 88.9점???
            # 분명 start와 ball이 동일할 때는 없다고 했는데?
            # 확인필요.
            if startX > x:
                minimum = min(cal_distance(startX, startY, x, -y),
                              cal_distance(startX, startY, 2 * m - x, y),
                              cal_distance(startX, startY, x, 2 * n - y))
            else:
                minimum = min(cal_distance(startX, startY, -x, y),
                              cal_distance(startX, startY, x, -y),
                              cal_distance(startX, startY, x, 2 * n - y))
        else:
            minimum = min(cal_distance(startX, startY, -x, y),
                          cal_distance(startX, startY, x, -y),
                          cal_distance(startX, startY, 2 * m - x, y),
                          cal_distance(startX, startY, x, 2 * n - y))
        answer.append(minimum)

    return answer