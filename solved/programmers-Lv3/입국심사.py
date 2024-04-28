"""
    n=5, times=[6, 17]
    6  17    6  17
    6        6
    6        6  17
    6
    -----    -----
    24초      34초
"""
def process(time, times):
    count = 0
    for t in times:
        count += time // t
    return count

def solution(n, times):
    time = 0
    bonus = 1
    while process(time + bonus, times) < n:
        bonus *= 2
    while bonus >= 1: # 직전 1단위까지 더해줌.
        while process(time + bonus, times) < n: # 직전까지만 수행
            time += bonus
        bonus = bonus // 2

    return time + 1 # 마지막에 + 1