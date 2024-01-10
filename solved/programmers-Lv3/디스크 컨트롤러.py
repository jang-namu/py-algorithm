from heapq import heappush, heappop

def solution(jobs):
    jobs.sort()
    time = 0
    acc = 0
    shortest_executable_jobs = []
    for job in jobs:
        while job[0] > time:
            if not shortest_executable_jobs:
                time = job[0]
                break
            selected_job = heappop(shortest_executable_jobs)
            time += selected_job[0]
            acc += time - selected_job[1]
        heappush(shortest_executable_jobs, (job[1], job[0]))

    while shortest_executable_jobs:
        selected_job = heappop(shortest_executable_jobs)
        time += selected_job[0]
        acc += time - selected_job[1]

    answer = acc / len(jobs)
    return int(answer)