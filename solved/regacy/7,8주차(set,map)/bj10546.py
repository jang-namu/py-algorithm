# 10546 배부른 마라토너
import sys
input = sys.stdin.readline

N = int(input())
maraton = dict()
for _ in range(N):
    name = input()
    maraton[name] = maraton.get(name, 0) + 1

for _ in range(N-1):
    name = input()
    maraton[name] -= 1

for name, goal in maraton.items():
    if goal == 1:
        print(name)
        break


