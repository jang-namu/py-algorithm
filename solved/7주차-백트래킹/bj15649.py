# 15649 N과 M (1)
import sys
input = sys.stdin.readline


def makeProgression(s, e):
    while 1:
        tmp = []
        comp = progressions[-1]
        for i in range(1, n+1):
            if len(tmp) == m:
                progressions.append(tmp)
                break
            if i not in tmp:
                tmp.append(i)
        if progressions[-1] == list(n for n in range(n, 0, -1)):
            break


n, m = map(int, input().split())
progressions = []
print(progressions)
