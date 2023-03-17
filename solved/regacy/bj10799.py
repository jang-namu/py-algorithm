# 10799 쇠막대기
"""
    ( 가 나오면 막대기 추가, ()가 연속으로 나오면 자름(len(stack)만큼 더한다.)
    )가 연속으로 '())'과 같은식으로 나오면 막대기 하나가 끝난 것. + 1
"""
import sys
input = sys.stdin.readline

stack = []
stick = 0
sign = False

for ele in input().rstrip():
    if ele == '(':
        sign = False
        stack.append('(')
    else:
        stack.pop()
        if sign:
            stick += 1
        else:
            stick += len(stack)
        sign = True

print(stick)
