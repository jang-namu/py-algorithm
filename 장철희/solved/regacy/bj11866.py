# 11866 요세푸스 문제 0
from queue import Queue

N, K = map(int, input().split())
people = Queue()
for i in range(1, N+1):
    people.put(i)
tmp = Queue()
res = []

while people.qsize():
    for i in range(K-1):
        if people.qsize() == 0:
            while tmp.qsize():
                people.put(tmp.get())
        tmp.put(people.get())
    while tmp.qsize():
        people.put(tmp.get())
    res.append(people.get())

print("<" + ", ".join(map(str, res))+">")