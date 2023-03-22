# 18258 큐 2
# queue와 리스트는 선형으로 되어있다.
# 따라서 pop()연산을 수행할 때, 남음 모든 원소를 한칸씩 당겨줘야 한다. O(n)
# 이 문제는 모든 명령이 O(1)시간에 이뤄져야 해결할 수 있다.
# collections의 deque 자료구조는 연결리스트로 구현되어 있어, 이러하 문제점을 해결할 수 있다. O(1)
import sys
from collections import deque
input = sys.stdin.readline

queue = deque()
res = []
T = int(input())
for _ in range(T):
    com = input().split()
    command = com[0]
    if command == "push":
        queue.append(int(com[1]))
    if command == "pop":
        res.append(queue.popleft() if queue else -1)
    if command == "size":
        res.append(len(queue))
    if command == "empty":
        res.append(0 if len(queue) else 1)
    if command == "front":
        res.append(queue[0] if queue else -1)
    if command == "back":
        res.append(queue[-1] if queue else -1)
print("\n".join(map(str, res)))
