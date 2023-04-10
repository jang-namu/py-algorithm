# 2467 용액
"""
    두 수의 합의 절대값이 최소가 되게 하려면, 절대값 순으로 정렬한 뒤 연달아 오는 두개의 원소들의 합(절대값)을 비교한다.
    어떤 두 수의 합의 절대값이 최소이기 위해선, 두 수의 절대값은 비슷해야하기 때문이다.
"""
import sys
input = sys.stdin.readline

n = int(input())
liquid = list(map(int, input().split()))
liquid.sort(key=lambda x: abs(x))

minimum = 1e11
li = [0, 0]
for i in range(n-1):
    if minimum > abs(liquid[i] + liquid[i+1]):
        minimum = abs(liquid[i] + liquid[i + 1])
        li[0] = liquid[i]
        li[1] = liquid[i+1]

print(*sorted(li))  # 정렬해서 출력