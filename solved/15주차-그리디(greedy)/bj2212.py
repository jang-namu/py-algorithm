# 2212 센서
"""
    어떻게하면 각 영역의 길이를 최소화 할 수 있을까?
    => 답이 쉽사리 안 떠오름
    해결 => 우리가 구하는건 센서 간의 거리의 최소 합
            센서의 '위치'보다는 '센서 간의 거리'에 집중.
            집중국이 두 개 이상일 때에는, 센서 간 거리 중 가장 긴 거리를 분리시킨다.(제외)

    가장 긴 거리를 뺀 최적해가 존재하는가
    => 가장 긴 거리를 포함한 최적해가 있다고 가정.
    => 긴거리 제외하고 반대쪽 짧은 쪽을 넣어서 삽입하면 total 거리는 더 짧아진다. => 가장 긴 거리를 포함한 최적해는 존재할 수 없음.
"""
import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
sensors = list(map(int, input().split()))
sensors.sort()

if N <= K:          # 센서보다 집중국이 많으면 다 박으면 됨
    print(0)
else:
    total = sensors[-1] - sensors[0]        # 끝에서 끝까지 거리
    between_sensors = sorted([(sensors[i]-sensors[i+1]) for i in range(N-1)])   # 인덱싱 순서에 주의, 음수!!
    total = total + sum(between_sensors[:K-1])      # 음수이므로 더해주면 됨
    print(total)
    """
    between_sensors = sorted([(sensors[i+1]-sensors[i]) for i in range(N-1)])       # 인덱싱 순서가 반대, 양수!
    print(sum(between_sensors[:N-K]))
    """
