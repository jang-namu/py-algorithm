# 1826 연료 채우기
"""
    2023.05.14
    변수명 참조 제대로 확인하자.

    요약: 현재 연료로 갈 수 있는 거리(pos) 안에서 가장 많은 연료를 가진 station에 방문.
            연료 충전 후, 마을 도달 or 거리 내 남은 station이 없을 때(실패) 까지 반복.
"""
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())

station = [tuple(map(int, input().split())) for _ in range(N)]  # (출발지부터 거리, 연료양)
station.sort()

efficient_station = []              # 현재 거리 내 주요소 중 가장 많은 연료를 뽑기위해 힙큐 사용
L, P = map(int, input().split())    # (마을 거리, 현재 연료양)

pos = P    # position, 현재 연료로 갈 수 있는 위치
answer = 0  # 방문 수
idx = 0     # 현재 힙에 저장된 주유소 + 1
while pos < L:    # 마을 도착 시 종료
    while idx < N and station[idx][0] <= pos:
        heappush(efficient_station, -station[idx][1])   # 가장 큰 수가 필요 -> 음수로 저장
        idx += 1
    if not efficient_station:   # 모든 주유소 방문 시 or 더 이상 갈 수 있는 주유소가 없을 시
        break
    pos += -heappop(efficient_station)
    answer += 1

answer = answer if pos >= L else -1
print(answer)
