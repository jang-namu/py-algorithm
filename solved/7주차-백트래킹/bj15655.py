# 15655 N과 M (6)
"""
import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = sorted(map(str, input().split()), key=int)
print('\n'.join(map(' '.join, combinations(numbers, M))))
"""


"""
    좀 더 표준 함수다운 작성법.
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = sorted(map(int, input().split()))


def make_combinations(N, M, seq='', length=0, idx=0):
    if length == M:
        print(seq)
        return
    for i in range(idx, N):
        new_seq = seq + str(numbers[i]) + " "
        make_combinations(N, M, new_seq, length+1, i+1)
make_combinations(N, M)

"""
    백준 DFS에 원형에 더 까가운 풀이"""
"""
from sys import stdin


def get_two_input():
    a, b = map(int, stdin.readline().split(" "))
    return a, b


def dfs(a, b):
    if b == m:
        print(' '.join(print_nums))
        return
    for i in range(a, len(nums)):
        if checks[i]:
            continue
        checks[i] = True
        print_nums[b] = str(nums[i])
        dfs(i + 1, b + 1)
        checks[i] = False


if __name__ == '__main__':
    n, m = get_two_input()
    nums = list(map(int, stdin.readline().split(" ")))
    nums.sort()
    print_nums = ['0' for _ in range(m)]
    checks = [False for _ in range(n)]
    dfs(0, 0)
"""