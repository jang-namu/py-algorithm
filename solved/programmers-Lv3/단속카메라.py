def solution(routes):
    answer = 0
    sorted_routes = sorted(routes, key=lambda x: (x[1], x[0]))

    answer += 1
    time = sorted_routes[0][1]

    for route in sorted_routes:
        if time >= route[0]:
            continue
        answer += 1
        time = route[1]

    return answer

