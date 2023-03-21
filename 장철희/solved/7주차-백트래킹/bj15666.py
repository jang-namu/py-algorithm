# 15666 N과 M (12)
"""
    비 내림차순 순열은 정렬된 number들의 조합을 이용해 만들 수 있다.
    같은 수를 중복으로 뽑기위해 combinations_with_replacement를 사용하며,
    같은 수가 여러개 들어올 것을 생각해 set로 numbers에서 중복을 제거했다.
    set를 사용하지 않을 경우, 같은 순열이 반복해서 나온다.
"""
"""
import sys
from itertools import combinations_with_replacement as cbwr
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(sorted(set(input().split()), key=int))
print('\n'.join(map(' '.join, cbwr(numbers, M))))
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = sorted(set(map(int, input().split())))    # list로 감싸면 더 느려진다.
new_N = len(numbers)  # 중복제거한 만큼 길이가 준다.


def print_permutations(seq='', idx=0, m=0):
    if m == M:
        print(seq)
        return
    for i in range(idx, new_N):
        new_seq = seq + str(numbers[i]) + ' '
        print_permutations(new_seq, i, m + 1)


print_permutations()