# 7579 앱
"""
백준풀이, 메모리가 100만까지 주어질 수 있다. 메모리를 기준으로 최소 cost를 계산하기에는 for 반복문이 많아 너무 느리다.
따라서, costs를 기준으로 최대 메모리 확보량을 구한다.
index는 cost를 의미하고 값은 최대 확보가능한 메모리를 의미한다.
최종 dp에는 구해지지 않고 초기값 '-1'이 그대로인 값들도 있다. 이는 cost의 조합으로 만들 수 없기 때문이다.
의미적으로 본다면 '-1'로 나오는 값들은 그 이전 인덱스의 값과 같다. 또한, 최종 출력 시 앞에서부터 검사하여
최초 M이 나올 때를 출력하기 때문에 '-1'이 나오는 것은 의도에 맞게 무시된다.
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))

limit = sum(costs)
dp = [-1] * (limit + 1)
dp[0] = 0

for memory, cost in zip(memories, costs):
    for i in range(limit, cost-1, -1):
        if dp[i-cost] != -1 and dp[i-cost] + memory > dp[i]:
            dp[i] = max(dp[i-cost] + memory, dp[i])
# print(dp)
for i in range(limit + 1):  # 확보가능한 메모리가 M보다 클때, 앞에서부터 cost(인덱스)는 증가하므로, 최초 나온걸 출력
    if dp[i] >= M:
        print(i)
        break


"""
    # for문 범위지정 역시나 느림
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))

dp = [100001] * (M+1)
dp[0] = 0  
length = 0
for memory, cost in zip(memories, costs):
    length = length + memory
    length = M if length > M else length
    for i in range(length, 0, -1):
        if i >= memory:
            dp[i] = min(dp[i-memory] + cost, dp[i])
        elif dp[i] > cost:
            dp[i] = cost
for i in range(M//10 + 1):
    print(i, dp[i*10:i*10+10])
print(dp[-1])
"""

"""
# 정답이긴한데,,, 속도가 너무 느림
# 아이디어 : M~memory 까지는 이전 값과 새로운 값을 비교해서 최소
# meymory보다 작은 경우엔 해당 앱을 비활성화 or 그 전 더 작은 비용의 앱을 종료 min 선택
# dp는 메모리당 최소 코스트
# 이 문제의 어려운 점은 16493 최대페이지수 문제와 달리, iteration마다 해당 앱의 메모리 "이하"만 비용이 결정됨.
# 또한, iteration이 증가할 때마다 이전에 체크한 범위만큼 범위를 늘려나가야 함.
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))

dp = [100001] * (M+1)
dp[0] = 0

for memory, cost in zip(memories, costs):
    for i in range(M, memory-1, -1):
        if dp[i-memory] != 100001:
            dp[i] = min(dp[i], dp[i-memory] + cost)

    memory = M if memory > M else memory    # memory가 M보다 크면 index out of range 발생
    for i in range(1, memory + 1):
        dp[i] = min(dp[i], cost)
print(dp[-1])
"""








