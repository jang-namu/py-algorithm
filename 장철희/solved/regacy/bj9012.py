# 9012 괄호
"""
# 이렇게 섹시할수가.. replace 문자열! 대치!
import sys
vps = sys.stdin.readlines()[1:]
for v in vps:
	v = v.rstrip()
	while '()' in v:
		v = v.replace('()', '')
	if v:
		print('NO')
	else:
		print('YES')
"""

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    stack = list()
    sign = False
    for ele in input().rstrip():
        if ele == '(':
            stack.append(0)
        elif stack:
            stack.pop()
        else:
            sign = True
            break

    print("NO" if stack or sign else "YES")