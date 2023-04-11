# 1406 에디터
import sys
input = sys.stdin.readline

ans = list(input().rstrip())
m = int(input())
arr = []
for _ in range(m):
    a = input().split()
    if a[0] == 'L':    # 왼
        if ans:
            arr.append(ans.pop())
    elif a[0] == 'D':  # 오
        if arr:
            ans.append(arr.pop())
    elif a[0] == 'B': # 삭제
        if ans:
            ans.pop()
    else:
        ans.append(a[1])

while arr:
    ans.append(arr.pop())
print(''.join(ans))
