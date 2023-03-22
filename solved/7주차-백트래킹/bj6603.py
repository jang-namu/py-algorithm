# 6603 로또
"""
    단순 정렬된 조합을 구하는 문제, S의 원소는 원래부터 오름차순으로 주어지므로 따로 정렬할 필요도 없다.
    종료조건에 input()[0] == 0으로 비교해야지, 그냥 input() == '0'해도 항상 False가 나오기 때문에 종료안됨.
"""
import sys
from itertools import combinations
input = sys.stdin.readline

while True:
    array = list(map(str, input().split()))
    if len(array) == 1:
        break
    array = array[1:]
    for lst in combinations(array, 6):
        print(' '.join(lst))
    print()


