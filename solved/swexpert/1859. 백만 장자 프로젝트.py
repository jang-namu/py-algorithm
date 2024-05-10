T = int(input())

for seq in range(1, T+1):
    result = 0
    N = int(input())
    lst = list(map(int, input().split()))
    max_price = [0] * N
    max_price[-1] = lst[-1]

    for i in range(1, N):
        idx = N - i - 1
        max_price[idx] = max(lst[idx], max_price[idx + 1])

    for i, p in enumerate(lst):
        if p < max_price[i]:
            result += max_price[i] - p
    print(f"#{seq} {result}")