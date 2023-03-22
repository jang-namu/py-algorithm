# 10828 스택
"""파이썬에서 스택은 리스트로 이미 구현되어 있음"""
import sys
input = sys.stdin.readline

N = int(input())
stack = list()

for _ in range(N):
    command = input().split()
    if "push" in command:
        stack.append(int(command[1]))
    elif "pop" in command:
        print(stack.pop() if stack else -1)
    elif "size" in command:
        print(len(stack))
    elif "empty" in command:
        print(0 if stack else 1)
    elif "top" in command:
        print(stack[-1] if stack else -1)