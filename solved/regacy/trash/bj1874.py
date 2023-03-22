# 1874 스택 수열
import sys
input = sys.stdin.readline

N = int(input())
stack = list()
idx = 1
ans = []
for _ in range(N):
    target = int(input())
    while target >= idx:
        stack.append(idx)
        ans.append('+')
        idx += 1
    if stack.pop() == target:
        ans.append('-')
    else:
        print('NO')
        exit()

print('\n'.join(ans))