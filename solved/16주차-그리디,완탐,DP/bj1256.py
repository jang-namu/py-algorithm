# 1256 사전
"""
    nCr, combination의 갯수를 이용한다.
     n개는 'a', m개는 'b'로, 총 n+m개의 문자로 이루어진 문자열이다.
     a=0, b=1로 생각하고 n=3, m=3일 경우 오름차순 정렬한 결과는 아래와 같다.
     000111             여기서, 규칙을 찾았다. '111'은 m개의 문자 중 m개 선택하는 mCm

     001011     1
     001101     2
     001110     3        최상위 1 이하의 3개의 문자 존재. n=1, m=2 => 3C2 = 3

     010011     1
     010101     2
     010110     3
     011001     4
     011010     5
     011100     6        최상위 1 이하 4개 문자 존재. n=2, m=2 => 4c2=6

     100011              ~
     ...


"""
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())


def nCr(n, r):
    r = min(r, n-r)
    ans = 1
    for i in range(r):
        ans *= (n-i)
        ans /= (i+1)
    return ans


if K > nCr(N+M, M):     # 애초에 생기는 단어의 수보다 높은 수를 입력받았을 때
    print(-1)
    exit(0)

result = ""     # 결과 문자열을 만드는 변수
key = 0         # 현재 확정지은 문자를 의미. key + rg >= K이면, 넘어섰다는 의미이므로 이전 iter의 상위 문자는 확정.
restN = N       # 남은 'a' 갯수
restM = M       # 남은 'z' 갯수
while restN > 0 and restM > 0:      # 둘 중 하나가 0이면 종료.
    key += 1    # (restM)C(restM)의 역할
    if key == K:    # 번호 찾으면 남은 'a'전부 소비 후 종료
        result += "a" * restN
        restN = 0
        break
    for i in range(restN):
        rg = nCr(restM+i, restM-1)  # rg는 현재 iter에서 nCr로 넘어가는 번호 수
        if key + rg >= K:   # 초과하면, 이전 iter까지만 확정.
            result += "a" * (restN-i-1)
            result += "z"
            restN -= (restN-i-1)
            restM -= 1
            break
        key += rg

result += "a" * restN   # 둘 중 하나가 0이면 문자열 뒤에 나머지를 전부 채움
result += "z" * restM
print(result)