"""
(r,c)포인트 1~n
운송경로: m개 포인트 순서대로 방문
로봇: x개, 0초에 동시 출발
- 로봇 1초마다 움직임 [[1,0],[-1,0],[0,1],[0,-1]]
- 포인트 간 이동은 최단경로
    - 최단경로 중에서 r좌표 이동을 우선

같은 좌표에 로봇 2대 이상 모이면 충돌 위험
Goal: 위험 상황이 총 몇 번 일어나는지 (어떤 시간에 여러 좌표에서 위험 상황이 발생한다면 그 횟수를 모두 더함)
"""


# routes[i]의 길이는 모두 같습니다.
"""
풀이:
매 턴 마다 
- 각 로봇을 한 칸씩 이동한다.
- 모든 로봇이 이동하면 맵을 만들어 충돌 지역을 확인해서 더해준다.
- 중간에 완료지점에 도착한 로봇은 제거한다.
"""
def solution(points, routes):
    answer = 0
    x = len(routes)  # 로봇 수
    m = len(routes[0])  # 경로에 포함된 포인트 수
    robots = [tuple(points[route[0] - 1]) for route in routes]
    reached = [0] * x

    answer += countIfCrashed(robots)
    while len(robots) > 0:
        count = 0
        remove = []
        for r in range(len(robots)):
            if reached[r] == m - 1:  # 이미 완료됐으면 넘김
                remove.append(r)
                continue

            # r번째 로봇 이동
            next = points[routes[r][reached[r] + 1] - 1]

            if robots[r][0] != next[0]:
                if robots[r][0] > next[0]:
                    robots[r] = (robots[r][0] - 1, robots[r][1])
                else:
                    robots[r] = (robots[r][0] + 1, robots[r][1])
            else:
                if robots[r][1] > next[1]:
                    robots[r] = (robots[r][0], robots[r][1] - 1)
                else:
                    robots[r] = (robots[r][0], robots[r][1] + 1)

            if robots[r][0] == next[0] and robots[r][1] == next[1]:
                reached[r] += 1

        for r in remove[::-1]:
            robots.pop(r)
            reached.pop(r)
            routes.pop(r)
        answer += countIfCrashed(robots)
    return answer


def countIfCrashed(robots):
    count = 0
    d = dict()
    for robot in robots:
        d[robot] = d.get(robot, 0) + 1

    for e in d.values():
        if e > 1:
            count += 1
    # print(robots, d)
    return count
