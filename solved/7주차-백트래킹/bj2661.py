# 2661 좋은수열

# 백준 참고 수정.ver
N = int(input())


def check(seq):
    for i in range(1, len(seq)//2 + 1):
        if seq[-i:] == seq[-2 * i:-i]:
            return False
    return True


def make_good_permutation(seq='', length=0):
    if length == N:
        print(seq)
        exit(0)

    for i in range(1, 4):
        new_seq = seq + str(i)
        if check(new_seq):
            make_good_permutation(new_seq, length+1)


make_good_permutation()




"""
    아이디어 : 1. 현재 추가되는 값은 바로 이전에 추가된 값과 달라야한다.
               2. 수를 하나씩 추가할 때마다, 맨 앞에서부터 절반씩 잘라가며, 추가한 원소를 포함해
                  인접한 두 수열이 같진 않은지 확인한다.

    어려웠던 점 : for문에서 인덱스를 설정하는게 까다로웠다.
                    size를 구할 때, (length -1) // 2 부터 시작해야 size가 idx보다 갯수가 많아지는 것을 막을 수 있다.
"""
"""
N = int(input())
def make_good_permutation(seq='', length=0):
    if length == N:
        print(seq)
        exit(0)
    for i in range(1, 4):
        if length > 0 and str(i) == seq[-1]:
            continue

        sign = False
        start = 0 if length % 2 else 1
        for idx, size in zip(range(start, length - 1, 2), range((length-1) // 2, 0, -1)):
            #print(length, idx, size)
            if seq[idx:idx+size+1] == seq[idx+size+1:] + str(i):
                sign = True
                break

        if sign:
            continue

        new_seq = seq + str(i)
        make_good_permutation(new_seq, length+1)


make_good_permutation()
"""