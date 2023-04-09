# 2632 피자판매
"""
    2143과 유사한 문제. 해당 문제에선 bisect를 이용해 딕셔너리 B에 키값을 찾았다.
    생각해보면, 딕셔너리에 get을 이용하면 더 빠른 O(1) 시간안에 해당하는 키값이 있는지 확인이 가능하다.
"""
import sys
input = sys.stdin.readline

customer = int(input())
m, n = map(int, input().split())
pizzaA = list(int(input()) for _ in range(m))
pizzaB = list(int(input()) for _ in range(n))

subsetA = dict()
for i in range(m):
    subset_sum = 0
    for j in range(i, m+i):     # 모듈로 연산으로 배열을 원형으로 사용한다..
        subset_sum += pizzaA[j % m]
        if subset_sum > customer:   # 음수의 조각은 없으므로 break 할 수 있다.
            break
        subsetA[subset_sum] = subsetA.get(subset_sum, 0) + 1

subsetB = dict()
for i in range(n):
    subset_sum = 0
    for j in range(i, n+i):
        subset_sum += pizzaB[j % n]
        if subset_sum > customer:
            break
        subsetB[subset_sum] = subsetB.get(subset_sum, 0) + 1

subsetA[sum(pizzaA)] = 1       # 0에서 시작해서 m-1까지(포함)와, 1에서 시작해서 0까지(포함)는 같은 경우이다.
subsetB[sum(pizzaB)] = 1       # 즉, 모든 조각을 포함하는 경우는 1가지

subsetA[0] = 1      # 한 쪽 피자로만 주문이 이루어질 경우
subsetB[0] = 1

ans = 0
for a in subsetA.keys():        # a에 대해, B에서 a+b = customer를 만족하는, b (customer - a)를 찾는다.
    ans += subsetA[a] * subsetB.get(customer-a, 0)
print(ans)
