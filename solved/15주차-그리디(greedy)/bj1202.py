# 1202 보석 도둑
"""
    2023.05.14
    처음 접근법: 가장 비싼 보석부터 넣을 수 있는, 가장 작은 가방에 넣는다.
    => 문제, 비싼 보석을 넣을 가장 작은 가방을 찾아야 함. 이 과정에서 쉽사리 O(n^2)이 된다. => 시간초과
    두번쩨: 위에 방법에서 이진탐색을 통해 가장 작은 가방을 찾음.
    => 문제, 같은 가방에 들어갈 보석이 여러개이면? 또 비어있는 가방을 찾아야함.
    세번쨰: 딕셔너리로 가방을 관리, 이진탐색을 쓰기 위해 딕셔너리 정렬된 상태로저장(파이썬의 사전형은 순서기억)
    => 문제, 이진탐색 쓰려면 keys() 배열 필요 => 매번 del할때마다 새로운 배열 생성 =>  시간초과

    마지막!!: 주유소 문제와 동일. 가장 작은 가방부터 시작해서, 현재 넣을 수 있는 보석의 가치를 힙큐에 저장.
                비싼 보석부터 빼가면서 가방에 넣으면된다.
"""
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, k = map(int, input().split())
gems = [tuple(map(int, input().split())) for _ in range(n)]
gems.sort()

backpack = list(int(input()) for _ in range(k))
backpack.sort()

available_gems = []
ans = 0
idx = 0     # 현재 available_gems에 들어간 gem + 1 위치를 가리킴
for high in backpack:       # high는 현재 가방에 넣을 수 있는 무게(상한)
    while idx < n and gems[idx][0] <= high:
        heappush(available_gems, -gems[idx][1])
        idx += 1
    if not available_gems:      # 넣을 수 있는 보석이 없으면 다음 가방으로 넘어감
        continue
    ans += -heappop(available_gems)

print(ans)


"""
반례, 문제: dict가 정렬이 안됨    => 파이썬 3.6부터 딕셔너리가 순서 기억 => 정렬 후 저장 => 시간초과... (정렬때문은 아닌듯)
3 3
1 10
2 5
3 4
3
1
1
"""


"""
# 백준 naniri04
# 
import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split()) # gem=N, bag=K

gem = [tuple(map(int, input().split())) for _ in range(N)]
gem.sort(key=lambda x:x[0], reverse=True)

bag = list(int(input()) for _ in range(K))
bag.append(-1)      # 마지막 가방(empty)으로 -1이 선택되면, 그 때 남은 모든 보석을 돌아보며 가치가 낮은건 빼고 높은 것을 넣음
bag.sort()

heap = []
empty = bag.pop()   # 무거운 가방부터
for weight, value in gem:   # 무거운 보석부터
    if empty >= weight:
        heapq.heappush(heap, value)
        empty = bag.pop()
    else:
        if len(heap) == 0: continue
        cheapest = heapq.heappop(heap)      # 싼 보석은 빼고, 비싼 보석을 넣는다.
        if cheapest < value:
            heapq.heappush(heap, value)
        else:
            heapq.heappush(heap, cheapest)
print(sum(heap))
"""