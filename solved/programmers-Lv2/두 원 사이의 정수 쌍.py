"""
    문제 설명. r1과 r2 원에 들어가는 정수쌍 좌표를 각각 구해서 계산한다.

    2차원 상의 제 1사분면(원의 반의 반)만을 가정하고 구한 후 * 4를 하고 겹치는 부분을 빼준다.
    겹치는 부분: 원점은 4번 겹치게 되고, 원점을 제외한 x, y축 선상의 좌표는 각각 2번씩 들어가게 된다.
    문제점: 두 원에 들어가는 정수쌍 좌표를 따로 구하고 '뺄셈을 할 때', 작은원의 둘레에 포함되는 모든 점들을 다시 더해줘야 한다.
"""

import math

"""
    is_inside는 현재 정수쌍 좌표 (a, b)가 중심이 원점이고 반지름이 r인 원에 포함되는지 검증한다.
"""


def is_inside(r, a, b):
    valid = math.sqrt(a ** 2 + b ** 2)
    if r >= valid:
        return True
    return False


"""
    is_radius는 현재 정수쌍 좌표 (a, b)가 중심이 원점이고 반지름이 r인 '원에 둘레에' 위에 있는지 검증한다.
"""


def is_radius(r, a, b):
    valid = math.sqrt(a ** 2 + b ** 2)
    if r == valid:
        return True
    return False


"""
    원래 원의 반의 반. 즉, 1/4 크기의 원에 점이 몇 개 들어가는지 계산한다.
    첫 행의 triangle은 y = -x + r을 그었을 때, 그려지는 이등변 삼각형에 포함되는 점의 개수를 의미한다.
"""


def point(r):
    triangle = sum(range(1, r + 2))

    """
        (1, r) 부터 시작해서 height가 0이 되기 전까지, 즉 (0, r)이 되기 이전까지.
        점이 원의 밖에 있다면 height를 줄이면서 해당 x 좌표에서 추가적으로 세야하는 점이 몇 개 있는지 계산한다.
    """
    remain_height = r
    for remain_width in range(1, r + 1):
        while remain_height > 0:
            if is_inside(r, remain_height, remain_width):  # 원의 내부에 있다면
                triangle += remain_height - (r - remain_width)  # 앞서, 삼각형에서 계산한만큼은 뺀다.
                break
            remain_height -= 1

    return triangle * 4 - r * 4 - 3  # 1/4의 원을 구했으니 * 4를 하고, 겹쳐 들어간만큼 빼준다.


"""
    이 함수는 point와 비슷하지만, 작은 원에서 둘레 선상의 있는 정수쌍 좌표를 구한다. x, y축 선상의 좌표는 포함하지 않는다.   
    ([(r, 0), (-r, 0), (0, r), (0, -r)]는 solution에서 더해준다.)
"""


def radius_point(r):
    answer = 0
    remain_height = r
    for remain_width in range(1, r + 1):
        while remain_height > 0:
            if is_radius(r, remain_height, remain_width):
                answer += 1
                break
            elif is_inside(r, remain_height, remain_width):
                break
            remain_height -= 1
    return answer * 4


def solution(r1, r2):
    return point(r2) - point(r1) + radius_point(r1) + 4  # 4는 작은 원의 x, y좌표 (r, 0), (-r, 0), (0, r), (0, -r)