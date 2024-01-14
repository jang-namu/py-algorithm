from bisect import bisect_right

def solution(operations):
    answer = []
    length = 0

    for op in operations:
        if op[0] == 'I':
            v = int(op[2:])
            answer.insert(bisect_right(answer, v), v)
            length += 1
            continue
        if length == 0:
            continue
        length -= 1
        if op[-2] == '-':
            answer.pop(0)
            continue
        answer.pop()

    if length == 0:
        return [0, 0]
    return [answer[-1], answer[0]]
