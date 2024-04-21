def solution(people, limit):
    people.sort(reverse=True)
    answer = 0

    s = 0
    e = len(people) - 1

    while s <= e:
        if people[s] + people[e] <= limit:
            e -= 1
        s += 1
        answer += 1

    return answer