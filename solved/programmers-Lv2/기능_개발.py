def solution(progresses, speeds):
    answer = []

    length = len(progresses)
    if length == 0:
        return answer

    start = 0
    while start < length:
        mulx = max(0, int(((100 - progresses[start]) + speeds[start] - 1) / speeds[start]))
        count = 0
        for i in range(start, length):
            progresses[i] += speeds[i] * mulx

        for i in range(start, length):
            if progresses[i] >= 100:
                count += 1
                start += 1
            else:
                break
        answer.append(count)

    return answer