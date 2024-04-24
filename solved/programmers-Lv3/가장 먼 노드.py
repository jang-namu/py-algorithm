def solution(n, edge):
    matrix = [[] for _ in range(n + 1)]
    for ed in edge:
        matrix[ed[0]].append(ed[1])
        matrix[ed[1]].append(ed[0])

    visited = [False] * (n + 1)

    q = [1]
    visited[1] = True

    while len(q) > 0:
        length = len(q)
        for _ in range(length):
            current = q.pop(0)
            for next in matrix[current]:
                if visited[next]:
                    continue
                visited[next] = True
                q.append(next)

    return length