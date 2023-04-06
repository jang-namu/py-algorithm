# 1747 소수&팰린드롬
"""
    에라토스테네스의 체를 이용해, 전체 소수 배열을 구했다.

    좀 더 최적화 되는 방법은 어떤 수가 소수인지 판단하는 함수를 작성하고, 이를 이용해 N부터 소수를 찾는것이다.
    또한, N//2까지가 아니라, sqrt(N)까지만 체에서 걸러내면 된다.

    증명, 소수가 아닌 N이 어떤 두 수 a * b라고 할 때, a와 b 둘 중 하나는 sqrt(N)보다 무조건 작다.
    두 수가 모두 sqrt(N) 보다 커지게 되면, 둘의 곱읍 N보다 커진다.
    어떤 수가 소수이기 위해선 N=a*b(a, b가 정수)는 불가능하다.
    따라서 N이하의 소수를 판별하는데에는 2~sqrt(N)의 배수만 확인하면 된다.

"""
"""
def eratosthenes(n):
    # 2부터 n까지의 모든 정수를 담는 리스트를 만든다.
    sieve = [True] * ((n-1)//2+1)   # 짝수는 모두 2의 배수이므로 짝수는 제거한다.
    
    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사한다.
    m = int(n ** 0.5)
    for i in range(3, m+1, 2):
        if sieve[i//2]:           # i가 소수인 경우
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    
    # 소수 목록 산출
    primes = [2] + [i*2+1 for i in range(1, (n-1)//2+1) if sieve[i]]    # 2를 제외한 짝수는 존재하지 않으므로 홀수로 구성한다.
    return primes
"""
import sys
input = sys.stdin.readline

N = int(input())
nums = [*range(1003002)]
nums[0] = nums[1] = 0
for i in range(2, 1003002//2):
    if nums[i] == 0:
        continue
    for j in range(i*2, 1003002, i):
        nums[j] = 0


def check(num):
    strNum = str(num)
    for i in range(len(strNum)//2):
        if strNum[i] != strNum[-i-1]:
            return False
    return True


for num in nums[N:]:
    if num == 0:
        continue
    if check(num):
        print(num)
        break