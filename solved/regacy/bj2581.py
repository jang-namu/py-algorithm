# 2581 소수
"""
    에라토스테네스의 체 : 2의 배수 제거 -> 3의 배수 제거 -> (4는 2의 배수이므로 제거됨) -> 5의 배수 제거 ->
    방식으로 소수를 찾을 수 있다.
"""
a = int(input())
b = int(input())

visited = [*range(b+1)]
visited[1] = 0
for i in range(2, int(b/2)+1):
    if not i:
        continue
    for j in range(i+i, b+1, i):
        visited[j] = 0

nums = [i for i in range(a, b+1) if visited[i]]

if nums:
    print(sum(nums))
    print(nums[0])
else:
    print(-1)


