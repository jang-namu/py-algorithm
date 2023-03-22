# 10773 제로
import sys
input = sys.stdin.readline

K = int(input())
li = list()
for _ in range(K):
    num = int(input())
    if num == 0:
        li.pop()
    else:
        li.append(num)
print(sum(li))
