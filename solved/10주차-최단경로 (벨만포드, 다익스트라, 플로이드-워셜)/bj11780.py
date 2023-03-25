# 11780 플로이드 2
"""
    중간 경로를 모두 구해야 한다.
    처음엔 node 배열을 만들어 중간 경로를 저장하고자, 최단경로가 만들어질 때마다 k를 저장했다.
    이 방법은 불완전해서 경로를 탐색하기 위해 순환적인 알고리즘이 필요하다.
    문제점은 앞에서 이미 만들어진 최단경로를 이용해 다른 최단경로를 만들어 낼 때 발생하는데,

    예를 들어 5->1->3의 경로가 앞에서 만들어지면 node[5][3]은 1이 된다.
    다만, 그 후에 4->3의 최단경로가 5를 지나야 하는 경우. 원래의 모든 경로는 4->5->1->3이지만
    k가 저장되는 방법으로는, node[4][3]은 5가 된다.
    즉, 가운데 경로가 소실된다.
    나는 이 문제를 탐색 과정에서 재귀적인 방법을 이용해 해결했다.
    mid를 구하고 mid와 end, start와 mid 사이 노드가 존재하는지 재귀적인 방법으로 확인해서 해결했다.

    사실 처음부터 node[r][c]에 버스가 존재할 때, r을 저장해놓고 최단경로가 만들어질 때,
    k가 아닌 node[k][j]를 저장하는 방법으로 처리하면, 배열의 모든 요소가 경로상 바로 이전 노드를 가리키기 때문에
    반복적인 방법으로 경로를 더 쉽게 탐색할 수 있다.
"""
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
dist = [[1e16] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b, w = map(int, input().split())
    dist[a][b] = min(dist[a][b], w)
for i in range(1, N + 1):
    dist[i][i] = 0

# r -> c로의 최단경로를 새로 만들 때, 중간노드를 저장하는 배열.
node = [[0] * (N + 1) for _ in range(N + 1)]


def floyd_warshall():
    for k in range(1, N + 1):  # 중간노드
        for i in range(1, N + 1):  # 출발노드
            for j in range(1, N + 1):  # 도착노드
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    node[i][j] = k
                    # k를 저장하는 것과 다르게 node[k][j]를 저장하게 되면,
                    # 내 코드랑은 다르게, node 배열의 값이 모두 경로상 바로 이전 노드를 가리킨다.
                    # 즉, 순환을 통해 앞 뒤를 탐색할 필요없이, 경로의 끝부터 처음 방향으로, 쉽게 탐색이 가능하다.
                    # node[i][j] = node[k][j]


# start부터 end까지 최단경로에 포함된 모든 노드의 리스트를 반환한다.
# 순환적 방법으로 경로를 짤라가며, 중간 노드가 있는지 확인한다.
def get_mid_path(start, end):
    mid = node[start][end]
    ans = []
    if node[mid][end]:
        ans += get_mid_path(node[mid][end], end)
        ans += [node[mid][end]]
        ans += get_mid_path(mid, node[mid][end])
    if mid != 0:
        ans += [mid]
    if node[start][mid]:
        ans += get_mid_path(node[start][mid], mid)
        ans += [node[start][mid]]
        ans += get_mid_path(start, node[start][mid])
    return ans


floyd_warshall()
for row in dist[1:]:
    ans = [i if i < 1e16 else 0 for i in row[1:]]
    print(' '.join(map(str, ans)))

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if dist[i][j] >= 1e16 or i == j:
            print(0)
            continue
        else:
            path = get_mid_path(i, j)
            print(len(path) + 2, i, *path[::-1], j)
