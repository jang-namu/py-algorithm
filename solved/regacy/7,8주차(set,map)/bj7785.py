# 7785 회사에 있는 사람
"""
# 딕셔너리로 저장. 입력받을 때마다 값(상태)을 바꾼다. set에 add remove가 더 빠른듯
import sys
input = sys.stdin.readline

N = int(input())
log = {}
for _ in range(N):
    name, where = input().split()
    log[name] = where

ans = []
for name, where in log.items():
    if where == "enter":
        ans.append(name)
print('\n'.join(sorted(ans, reverse=True)))
"""