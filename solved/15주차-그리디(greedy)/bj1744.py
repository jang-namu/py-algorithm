# 1744 수 묶기
"""
    양수: 큰것끼리 곱, 1은 무조건 곱하지 않음. (그냥 더한다.)
    음수 : 가장 큰것끼리부터 곱(양수가 됨), 음수가 짝수개=>짝지어서 곱하면 음수가 없음.
            홀수개면 절대값이 가장 작은수가 남음 => 0이있으면 곱하고, 없으면 결과에 포함
    0 : 음수가 홀수개일때, 가장 작은 음수를 0으로 만드는데 사용
"""
import sys
input = sys.stdin.readline

N = int(input())
nums = list(int(input()) for _ in range(N))
count_zero = nums.count(0)      # 0이 있는가
answer = nums.count(1)          # 1은 무조건 더한다.

nums.append(0)                  # 음수부와 양수부를 나누기 위한 0 삽입
nums.sort()
idx = nums.index(0)             # 첫번쨰로 나온 0의 위치

minus = nums[:idx]              # 음수
plus = [i for i in nums[idx+1:] if i > 1]   # 양수(1 제외)

for i in range(1, idx, 2):              # 음수끼리 곱
    answer += minus[i] * minus[i-1]
if idx % 2 and count_zero == 0:         # 홀수개일때
    answer += minus[-1]

for i in range(len(plus)-1, 0, -2):     # 양수끼리 곱
    answer += plus[i] * plus[i-1]
if len(plus) % 2:                       # 홀수개일 때
    answer += plus[0]

print(answer)
