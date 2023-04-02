# 1654 랜선 자르기
"""
    전체 범위에서 이진 탐색
    이진 탐색은 log N이므로 O(log(2**31) * K)의 시간복잡도를 갖는다.


"""
import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lans = [int(input()) for _ in range(K)]

start = 0
end = 2**31 - 1
while start <= end:
    mid = (start + end) // 2
    cnt = sum(lan // mid for lan in lans)
    if cnt >= N:    # =까지 달아준다. 현재 mid가 정답이어도, 이진탐색을 진행하면서 마지막에 end = mid-1 되고 종료된다.
        start = mid + 1
    else:
        end = mid - 1

print(end)