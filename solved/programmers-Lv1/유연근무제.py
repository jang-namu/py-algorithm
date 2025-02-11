# https://school.programmers.co.kr/learn/courses/30/lessons/388351
# 2025 프로그래머스 코드챌린지 1차 예선 유연근무제

def solution(schedules, timelogs, startday):
    answer = 0
    n = len(schedules)
    for i in range(0, n):
        target_hour, target_minute = safetime(schedules[i])
        if isSuccess(timelogs[i], target_hour, target_minute, startday):
            answer += 1
    return answer


def isSuccess(timelog, target_hour, target_minute, startday):
    date = startday % 7
    for time in timelog:
        if date == 6 or date == 0:  # 0 : 일요일
            date = (date + 1) % 7
            continue
        hour = time // 100
        minute = time % 100
        if (target_hour > hour) or (target_hour == hour and target_minute >= minute):
            date = (date + 1) % 7
            continue
        return False
    return True


def safetime(time):
    h = time // 100
    m = time % 100 + 10
    if m >= 60:
        h += 1
        m = m % 60
    return h, m