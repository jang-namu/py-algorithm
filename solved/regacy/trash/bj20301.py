# 20301 반전 요세푸스
"""
    pos 변수를 이용해 현재 포인터를 나타낸다.
    'len(num)이 K보다 작을 경우'. pos가 양수가 될 때 까지 더해줘야함!
"""
N, K, M = map(int, input().split())
num = [*range(1, N + 1)]

pos = 0
count = 0   # K개의 원소 뺀 횟수가 홀수인지 짝수인지 계산. 방향을 결정
while num:
    if (count // M) % 2:
        pos = pos - K
        if pos - K < 0:
            while pos < 0:
                pos += len(num)
        print(num[pos])
        num.pop(pos)
    else:
        pos = (pos + K - 1) % len(num)
        print(num[pos])
        num.pop(pos)
    count += 1


