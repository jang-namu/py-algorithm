# 2164 카드2
from collections import deque
N = int(input())
if N == 1:
    print(1)
    exit(0)

if N % 2:
    card = deque(list(i for i in range(2, N, 2)))
    card.append(card.popleft())
else:
    card = deque(list(i for i in range(2, N+1, 2)))

while len(card) > 2:
    card.popleft()
    card.append(card.popleft())

print(card[0] if len(card) == 1 else card[1])