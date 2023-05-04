# 11203 Numbers On a Tree
"""
    이진트리의 특징을 알면 쉽게 풀린다.
    포화 이진트리의 노드의 수는 2**n - 1 개이다.   # 이 문제에서는 루트를 실제 높이에 포함안했으므로 2**(n+1) - 1
    이 문제는 포화 이진트리에서 매기는 번호를 거꾸로 매겼다.
    즉, 원래 번호 + 이 문제에서의 번호 = 포화이진트리의 노드의 수가 성립한다.

    이진트리에서 왼쪽 자식은 부모노드 * 2
    오른쪽 자식은 부모노드 * 2 + 1 임을 이용한다.
"""
import sys
input = sys.stdin.readline

treeInfo = input().split()
if len(treeInfo) == 1:
    n = int(treeInfo[0])
    print(2**(n+1) - 1)
else:
    n = int(treeInfo[0])
    maxNodeNum = 2 ** (n+1)
    pos = 1
    for move in treeInfo[1]:
        if move == 'L':
            pos *= 2
        else:
            pos = pos * 2 + 1
    ans = maxNodeNum - pos
    print(ans)
