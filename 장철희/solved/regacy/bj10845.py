# 10845 큐
import sys
input = sys.stdin.readline

queue = []

def empty():
    return 1 if len(queue) == 0 else 0


def size():
    return len(queue)


def push(x):
    queue.append(x)


def pop():
    global queue
    if empty():
        return -1
    ans = queue[0]
    queue = queue[1:]
    return ans


def front():
    if empty():
        return -1
    return queue[0]


def back():
    if empty():
        return -1
    return queue[-1]


T = int(input())
for _ in range(T):
    command = input().strip()
    if "push" in command:
        _, x = command.split()
        push(int(x))

    if command == "pop":
        print(pop())

    if command == "size":
        print(size())

    if command == "empty":
        print(empty())

    if command == "front":
        print(front())

    if command == "back":
        print(back())
