# 11404 플로이드
"""
    플로이드-워셜 알고리즘
    매 라운드에서 새로 사용될 수 있는 중간노드를 골라, 경로를 줄여나간다.
"""
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
dist = [[1e10] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dist[i][i] = 0
for _ in range(m):
    a, b, w = map(int, input().split())
    dist[a][b] = min(dist[a][b], w)


def floyd_warshall():
    for k in range(1, n+1):     # 중간 경로
        for i in range(1, n+1):     # 출발 노드
            for j in range(1, n+1):     # 도착 노드
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])   # 중간 경로를 들렸다가면 더 짧아지는가


floyd_warshall()
for row in dist[1:]:
    ans = [i if i != 1e10 else 0 for i in row[1:]]
    print(' '.join(map(str, ans)))
