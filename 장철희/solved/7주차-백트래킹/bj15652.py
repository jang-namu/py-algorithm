# 15652 N과 M (4)
import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

N, M = map(int, input().split())
cb = combinations_with_replacement((list(str(i) for i in range(1, N+1))), M)
print('\n'.join(map(' '.join, cb)))

"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def combinations_re(sequence = "", length = 0, idx = 1):
    if length == M:
        print(sequence)
        return
    for num in range(idx, N+1):
        new_sequence = sequence + str(num) + " "
        combinations_re(new_sequence, length+1, num)

combinations_re()
"""