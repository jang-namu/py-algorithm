# 10162 전자레인지
T = int(input())

A = T // 300
T %= 300
B = T // 60
T %= 60
if T % 10:
    print(-1)
else:
    print(A, B, T // 10)