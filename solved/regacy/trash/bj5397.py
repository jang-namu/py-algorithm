# 5397 키로거
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    ans = []
    temp = []
    password = input().rstrip()
    for ch in password:
        if ch == '-':
            if ans:
                ans.pop()
        elif ch == '<':
            if ans:
                temp.append(ans.pop())
        elif ch == '>':
            if temp:
                ans.append(temp.pop())
        else:
            ans.append(ch)

    while temp:
        ans.append(temp.pop())
    print(''.join(ans))

