# 15961 회전 초밥
"""
    슬라이딩 윈도우와 딕셔너리 사용.(중복된 접시가 들어올 수 있고, 각 접시는 앞에서 추가하고 뒤에서 빼야하므로
    개수를 유지할 필요가 있다.)
    set으로 구현하게 될 경우, 개수에 대한 정보를 유지하지 못 하고 매번 새로운 set을 만들어야하므로 O(n*k)의 시간복잡도를
    띄게 되서 시간초과가 난다.

    슬라이딩 윈도우란, 투포인터와 유사히자만 그 특징으로 체크하는 범위의 길이가 고정된다는 점이다.
    매 iteration마다 전단에서 추가하고 후단에서 뺸다.
"""
import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = list(int(input()) for _ in range(n))
sushi += sushi[:k-1]    # 회전초밥은 원형테이블이다. 마지막원소에 다다르면 처음으로 돌아간다.
subset = dict()
subset[c] = 1
for i in range(k):
    subset[sushi[i]] = subset.get(sushi[i], 0) + 1

ans = len(subset)
for end in range(k, len(sushi)):
    subset[sushi[end]] = subset.get(sushi[end], 0) + 1
    subset[sushi[end-k]] -= 1
    if subset[sushi[end-k]] == 0:
        subset.pop(sushi[end-k])
    elif ans < len(subset):
        ans = len(subset)
print(ans)


"""
백준 풀이 : 각 초밥과 접시의 배열을 만들고, 범위 내 초밥이 들어오면 해당위치 + 1,
매번 legnth를 재지 않으며, 접시가 빠질 때, 초밥이 0 이되면 ans -= 1 한다.
또한 모듈로 연산을 이용해 원래 배열 범위 밖으로 나가도 인덱싱이 가능하도록 구현했다.
import sys
input = sys.stdin.readline

N, D, K, C = map(int, input().split())
plates = [0] * N

for i in range(N):
    plates[i] = int(input().strip())

sushi = [0] * (D + 1)
sushi[C] = float('inf')

cnt = 1

for i in range(K):
    if sushi[plates[i]] == 0:
        cnt += 1
    sushi[plates[i]] += 1

ans = cnt

for i in range(K, N + K - 1):
    #take off a plate
    if sushi[plates[i - K]] == 1:
        cnt -= 1
    sushi[plates[i - K]] -= 1

    #get next plate
    if sushi[plates[i % N]] == 0:
        cnt += 1
    sushi[plates[i % N]] += 1

    ans = max(ans, cnt)

print(ans)
"""