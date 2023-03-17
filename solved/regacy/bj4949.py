# 4949 균형잡힌 세상
import sys
input = sys.stdin.readline

pair = {')' : '(', ']' : '['}
while True:
    sentence = input().rstrip()
    if sentence == ".":
        break
    stack = list()
    sign = True

    for ch in sentence:
        if ch == '(' or ch == '[':
            stack.append(ch)
        elif ch == ']' or ch == ')':
            if not stack or stack.pop() != pair[ch]:
                sign = False

    print('yes' if sign and not stack else 'no')
