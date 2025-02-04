# https://school.programmers.co.kr/learn/courses/30/lessons/340212
"""
퍼즐 n개
퍼즐 has (난이도diff, 소요시간time_cur(이전 퍼즐:time_prev))
숙련도(level) = 틀리는 횟수

if diff <= level:
    spend time_cur
if diff > level:
    for _ in range(diff-level):
        spend (time_cur + time_prev) # 이전 퍼즐을 다시 풀땐 절대 안틀림
    spend time_cur

전체 제한 시간(limit)
limit 내에 모두 해결하기 위한 level의 최솟값(양수)
"""


# 이분 탐색
def solution(diffs, times, limit):
    base = 0  # limit 내에 퍼즐을 다 맞추는 (level-1)을 binary search로 찾음
    d = 50000  # diffs[i]의 최댓값 = 100000

    while d > 0:
        new_base = base + d
        if not calculateSpendingTime(diffs, times, new_base, limit):
            base = new_base
        else:
            d //= 2
    return base + 1


def calculateSpendingTime(diffs, times, level, limit):
    count = 0
    for i in range(len(diffs)):
        if diffs[i] <= level:  # diffs[0]은 무조건 1
            count += times[i]
        else:
            # 이전 퍼즐을 다시 풀땐 절대 안틀림
            count += (times[i] + times[i - 1]) * (diffs[i] - level)
            count += times[i]
        if count > limit:
            return False
    return True