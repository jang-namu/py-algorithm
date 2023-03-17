# 3986 좋은 단어
import sys
input = sys.stdin.readline

count = 0
for _ in range(int(input())):
    sentence = input().rstrip()
    stack = list()
    for ch in sentence:
        if not stack:
            stack.append(ch)
            continue
        if ch == 'A':
            if stack[-1] != ch:
                stack.append(ch)
            else:
                stack.pop()
        else:
            if stack[-1] != ch:
                stack.append(ch)
            else:
                stack.pop()
    if not stack:
        count += 1
print(count)