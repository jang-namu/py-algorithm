# 9095 1, 2, 3 더하기


""" 매우 중요!!! 아래 코드를 이해해보자.
    먼저 배열 c에 각각 1, 2, 3을 만드는 가짓수를 저장했다.
    for문에서 우선 4를 예로들면, 4를 만드는 가짓수는
    4를 만들기 위해 처음에 1을 선택한 가짓수(c[i-1])
    + 4를 만들기 위해 처음에 2을 선택한 가짓수(c[i-2])
    + 4를 만들기 위해 처음에 3을 선택한 가짓수(c[i-3])와 같다. """
T = int(input())
a = [int(input()) for _ in range(T)]
c = [0]*(11)
c[1] = 1
c[2] = 2
c[3] = 4
for i in range(4, 11):
    c[i] = c[i-1] + c[i-2] + c[i-3]
for b in a:
    print(c[b])

""" 단순한 재귀를 이용해 자연스럽게 해결
    기저조건 n==0과 n<0일 경우를 꼭 작성해야함"""
def makeNum(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return makeNum(n-1) + makeNum(n-2) + makeNum(n-3)

import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    print(makeNum(n))