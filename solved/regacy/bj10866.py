# 10866 덱
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
d = deque()
for _ in range(N):
    command = input().split()
    if len(command) > 1:
        if command[0] == "push_front":
            d.appendleft(int(command[1]))
        elif command[0] == "push_back":
            d.append(int(command[1]))
    elif command[0] == "pop_front":
        print(d.popleft() if d else -1)
    elif command[0] == "pop_back":
        print(d.pop() if d else -1)
    elif command[0] == "size":
        print(len(d))
    elif command[0] == "empty":
        print(0 if d else 1)
    elif command[0] == "front":
        print(d[0] if d else -1)
    elif command[0] == "back":
        print(d[-1] if d else -1)

"""
class Node:
    def __init__(self, item):
        self.data = item
        self.llink = None
        self.rlink = None
class Deque:
    def __init__(self):
        self.head = self
        self.tail = self
        self.cnt = 0

    def is_empty(self):
        return self.cnt == 0

    def is_full(self):
        return 0

    def appendleft(self, item):
        newnode = Node(item)
        newnode.llink = self.tail
        newnode.rlink = self.head
        self.head.llink = newnode
        self.tail.rlink = newnode
        self.cnt += 1
        self.head = newnode
        if self.tail == self:
            self.tail = newnode

    def append(self, item):
        newnode = Node(item)
        newnode.llink = self.tail
        newnode.rlink = self.head
        self.tail.rlink = newnode
        self.head.llink = newnode
        self.tail = newnode
        if self.head == self:
            self.head = newnode

    def popleft(self):
        data = self.head.data
        self.head = self.head.rlink
        self.head.llink = self.tail
        self.tail.rlink = self.head
        return data

    def pop(self):
        data = self.tail.data
        self.tail = self.tail.llink
        self.tail.rlink = self.head
        self.head.llink = self.tail
        return data


a = Deque()
for i in range(5):
    a.append(i)
    print(a.pop())
"""