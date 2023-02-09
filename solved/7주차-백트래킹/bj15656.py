# 15656 N과 M (7)
import sys
from itertools import product
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = sorted(input().split(), key=int)
print('\n'.join(map(' '.join, product(numbers, repeat=M))))


"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(sorted(map(int, input().split())))
permutations = []


def make_permutations(N, M, seq='', m=0):
    if m == M:
        permutations.append(seq)
        return
    for i in range(N):
        new_seq = seq + str(numbers[i]) + ' '
        make_permutations(N, M, new_seq, m+1)


make_permutations(N, M)
print('\n'.join(permutations))
"""