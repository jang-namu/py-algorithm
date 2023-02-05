# 15700 타일 채우기 4
"""
이 문제는 dp 타일링 문제가 아니다. 1x3일 때 dp타일링 문제에서는 경우의 수가 0이겠지만
이 문제는 최대 채울 수 있는 갯수를 물어본다.
아래 두줄짜리 풀이는 넓이를 이용해서 구한 것이다.
"""
n, m = map(int, input().split())
print((n*m)//2)


"""
패턴을 이용한 풀이. 내 풀이.
"""
"""
import sys
n, m = map(int, sys.stdin.readline().split())

if n % 2 and m % 2:
    if n > m:
        n, m = m, n
    print(n * (m-1)//2 + n//2)
else:
    print(n*(m//2) if m % 2 == 0 else m*(n//2))
"""