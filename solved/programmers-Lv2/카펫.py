def solution(brown, yellow):
    total = brown + yellow
    answer = []

    for x in range(brown, 1, -1):
        y = total / x
        if yellow == (x - 2) * (y - 2):
            answer = [x, y]
            break

    return answer