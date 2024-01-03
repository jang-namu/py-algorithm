def max_idx(lst):
    idx = 0
    length = len(lst)
    maximum = lst[0]
    for i in range(1, length - 1):
        if maximum < lst[i]:
            maximum = lst[i]
            idx = i
    return idx


def solution(priorities, location):
    answer = 0

    while True:
        answer += 1
        cutpoint = max_idx(priorities)
        if cutpoint == location:
            return answer

        if cutpoint == len(priorities) - 1:
            del priorities[-1]
            continue

        priorities = priorities[cutpoint + 1:] + priorities[:cutpoint]
        if location > cutpoint:
            location = location - (cutpoint + 1)
        else:
            # 위에서 먼저 priorities[cutpoint]를 리스트에서 제거했다.
            location = len(priorities) - cutpoint + location


"""



def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

"""
