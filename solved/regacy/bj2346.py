# 2346 풍선 터뜨리기

"""
    종이에 0은 적혀있지 않다.
"""
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
balloon = deque((i, ele) for i, ele in enumerate(map(int, input().split())))

move = balloon.popleft()
print(move[0]+1)
while balloon:
    if move[1] > 0:
        for _ in range(move[1]-1):
            balloon.append(balloon.popleft())
        move = balloon.popleft()
    else:
        for _ in range(abs(move[1])-1):
            balloon.appendleft(balloon.pop())
        move = balloon.pop()
    print(move[0]+1)