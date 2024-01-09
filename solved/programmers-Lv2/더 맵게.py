# NewOne = First + Second * 2

from heapq import heappush, heappop, heapify
def solution(scoville, K):
    answer= 0
    foods = scoville
    heapify(foods)
    length = len(foods)
    while foods[0] < K:
        first = heappop(foods)
        if length == answer+1:
            return -1
        second = heappop(foods)
        heappush(foods, first + second * 2)
        answer += 1
    return answer