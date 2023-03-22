# 14889 스타트와 링크
"""
    allstat - sum(l)은 l아닌 팀 - l인 팀 (사진 참조)
"""
import sys
from itertools import combinations as cb
N = int(sys.stdin.readline()) // 2
M = 2*N
stat = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
#print([i for i in zip(*stat)])  # 전치행렬
newstat = [sum(i) + sum(j) for i, j in zip(stat, zip(*stat))]
print(newstat)
allstat = sum(newstat) // 2
print(newstat[:-1])
mins = 65535
for l in cb(newstat[:-1], N):
    print(l)
    mins = min(mins, abs(allstat - sum(l)))
print(mins)


"""
    아이디어 : 백트래킹을 이용. team1에 들어가는 선수들을 먼저 구한 후, team1이 N//2명이 되면
    나머지는 team2로 계산해서 team1-team2의 실력차 return => min으로 비교
"""
"""
import sys
input = sys.stdin.readline

N = int(input())
players = list(list(map(int, input().split())) for _ in range(N))
players_index = [i for i in range(N)]
team1 = []
team2 = []

def make_team(num_of_players=0, total=0, idx=0):
    res = 10e9
    if num_of_players == N//2:
        global team2
        team2 = []
        team2_total = 0
        for i in range(N):
            if i in team1:
                continue
            for j in team2:
                team2_total += players[i][j] + players[j][i]
            team2.append(i)
        diff = abs(total - team2_total)
        #print(team1)
        #print(total, team2_total, diff)
        return diff

    for i in range(idx, N):
        new_total = total
        for j in team1:
            new_total += players[i][j] + players[j][i]

        team1.append(i)
        res = min(res, make_team(num_of_players+1, new_total, i+1))
        team1.pop()

    return res


print(make_team())
"""
