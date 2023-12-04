# 영화감독 숌


series = int(input())

MAX = 2e10
INT_MAX = int(MAX)

count = 0
for i in range(666, INT_MAX, 1):
    if str(i).__contains__('666'):
        count += 1
    if count == series:
        print(i)
        break
