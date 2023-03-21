# 10597 순열장난
"""
    아이디어 : 우선 N(num)을 구한다. 1~9까지는 한글자, 10이상부턴 2글자이니, 이를 이용하면 구할 수 있다.
    입력받은 number(망가진 순열)를 이용해 한글자 또는 두글자씩 res에 추가해가며 비교한다.
    여기까지 구현하고 나면, 그 후로는 시간을 줄이는 영역의 문제이다.
    1 or 2글자씩 추가할 때, 해당 숫자가 이미 res배열에 존재한다면 수행하지 않아도 된다. (무시)
    숫자를 비교해야하므로 문자열은 사용할 수 없다.
"""
import sys
input = sys.stdin.readline

numbers = str(input().strip())
length = len(numbers)
num = length if length < 10 else (length + 9) // 2
check = [i for i in range(1, num+1)]
res = []


def make_permutation(i=0):
    if len(res) == num:
        if sorted(res) == check:
            print(*res)
            exit(0)

    if i >= length:
        return

    one = int(numbers[i])
    if one not in res:
        res.append(one)
        make_permutation(i+1)
        res.pop()

    two = int(numbers[i:i+2])
    if two <= num and two not in res:
        res.append(int(numbers[i:i+2]))
        make_permutation(i+2)
        res.pop()

make_permutation()


"""
# 시간초과를 if numbers[i] not in seq: 으로 해결하려 했으나, 문자열에 경우에는, 10이 들어가고 1이 들어가도 포함된걸로 처리하는 문제발생
# ex) 10987612345 <= 정상 실행안됨. 이 문제를 해결하기 위해 다시 배열을 사용하는 방법으로 돌아갔다.  
import sys
input = sys.stdin.readline

numbers = str(input().strip())
length = len(numbers)
num = length if length < 10 else (length + 9) // 2
check = [str(i) for i in range(1, num+1)]

def make_permutation(seq='', i=0):
    print(seq)
    if seq.replace(" ", "") == numbers:

        if sorted(seq.split(), key=int) == check:
            print(seq)
            exit(0)
    if i >= length:
        return

    if numbers[i] not in seq:
        make_permutation(seq+numbers[i]+" ", i+1)

    two = numbers[i:i + 2]
    if int(two) <= num and two not in seq:
        make_permutation(seq+numbers[i:i+2]+" ", i+2)

make_permutation()
"""


"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

numbers = str(input().strip())
length = len(numbers)
num = length if length < 10 else (length + 9) // 2
check = [i for i in range(1, num+1)]
res = []


def make_permutation(seq=''):
    if len(seq)
        return
    elif seq == numbers:
        return res
    for i in range(num+1):
        new_seq = seq + str(i)
        res.append(str(i))
        a = make_permutation(new_seq)
        if a:
            break
        res.pop()

    return a

res = make_permutation()
print(' '.join(res))
"""