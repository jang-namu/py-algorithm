# 9576 책 나눠주기
"""
    치팅: 그리디, 마감시간이 작은 순으로 정렬. 만일 마감시간이 같다면, 시작시간이 작은 순으로 정렬
    왜 될까?
    => 마감시간이 작은 순으로 정렬하면, 해당 범위까지만 선택할 수 있는(전체에서 상대적으로 앞부분) 것을 선택하는 의미이다.
    왜 마감시간 다음, 시작시간이 '작은 순'으로 정렬해야할까?
    => 마감시간이 같다 = 기회의 상한은 같음, but 시작이 작은 순부터 채우면, 나중에 겹치서 못 주게 되는 인원이 있다고 해도,
    최대만큼 나눠줄 수 있게됨

    if, 시작시간 오름차순으로 정렬하면?
    => 3권의 책이 있고 (1, 3) (2, 2) (1, 2)가 있을 때, 시작시간 오름차순 정렬 (1, 2) (1, 3) (2, 2)로 두권밖에 주지못하고 3번 책은 사용 못함
    => but 마감시간 기준 (1, 2) (2, 2) (1, 3) 3권 다 쓸 수 있음.
"""
import sys
input = sys.stdin.readline

t = int(input())

ans = []
for _ in range(t):
    res = 0
    n, m = map(int, input().split())
    books = [False] * (n+1)
    people = []

    for _ in range(m):
        a, b = map(int, input().split())
        people.append((a, b))

    people.sort(key=lambda x: (x[1], x[0]))

    for a, b in people:
        for i in range(a, b+1):
            if not books[i]:
                books[i] = True
                res += 1
                break
    ans.append(res)
print('\n'.join(map(str, ans)))

"""
# 왜 안될까...
# 영역이 가장 짧은 순으로 정렬 후, 해당 영역에서 가장 적은 사람이 요구한 책을 준다.
import sys
input = sys.stdin.readline

t = int(input())

ans = []
for _ in range(t):
    res = 0
    n, m = map(int, input().split())
    books = [0] * (n+1)
    people = []

    for _ in range(m):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            books[i] += 1
        people.append((a, b))

    people.sort(key=lambda x: x[1]-x[0])

    for a, b in people:
        minimum = a
        for i in range(a+1, b+1):
            if books[minimum] > books[i]:
                minimum = i
       # print(books)
       # print(a, b, minimum, books[minimum])
        if books[minimum] < 10e6:
            books[minimum] = 10e9
            res += 1
            for i in range(a, b+1):
                books[i] -= 1
    ans.append(res)
print('\n'.join(map(str, ans)))
"""
