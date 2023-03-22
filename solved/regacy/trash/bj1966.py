# 1966 프린터 큐
"""
    구현으로 해결. 맨 앞에 오는 수가 가장 큰 수 일 때, obj면 종료. obj보다 큰 수 이면 popleft()
    둘 다 아닌 경우. 맨 뒤로 삽입
"""
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, pos = map(int, input().split())
    printer = list(map(int, input().split()))
    counter = dict()    # 딕셔너리 형식으로 중요도마다 개수저장.
    for ele in printer:
        counter[ele] = counter.get(ele, 0) + 1

    obj = printer[pos]  # 알고싶은 수
    printer[pos] = -1   # 수를 다른 값으로표시해둠.
    printer = deque(printer)    # 큐로 사용

    time = 1
    while True:
        MAX = max(counter)
        if obj == MAX and printer[0] == -1:
            break
        elif printer[0] == MAX:
            counter[printer[0]] -= 1
            if counter[printer[0]] == 0:
                counter.pop(printer[0], None)
            printer.popleft()
            time += 1
        else:
            printer.append(printer.popleft())

    print(time)