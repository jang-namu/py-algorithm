# 15990 1, 2, 3 더하기 5
""" 아이디어: 어떤수 n을 나타내는 경우의 수는
    n-1에서 1로 끝나지 않는 수 + n-2에서 2로 끝나지 않는 수 + n-3에서 3으로 끝나지 않는 수의 합으로 구할 수 있다.
    다시말해 마지막에 1을 뽑을 경우는 연속이되지 않기 위해, n-1에서 1로 끝나지 않는 수에 1을 더한 것과 같다."""
import sys
input = sys.stdin.readline
MOD = 1000000009

# 초기dp는 각각에서 1, 2, 3으로 끝나는 가짓수를 나타낸다.
# 1은 1만으로 만든다. 2도 2만으로 만든다. 3은 (2, '1'), (1, '2'), '3' 이므로 [1, 1, 1]이 된다.
# 각각 1로 끝나는 경우 2로 끝나는 경우, 3으로 끝나는 경우의 수를 2차원 배열로 저장하는 것을 유의깊게 보자!!
dp = [[1, 0, 0], [0, 1, 0], [1, 1, 1]]

for i in range(3, 100000):
    one = (dp[i-1][1] + dp[i-1][2]) % MOD
    two = (dp[i-2][0] + dp[i-2][2]) % MOD
    three = (dp[i-3][0] + dp[i-3][1]) % MOD
    dp.append([one, two, three])

T = int(input())
for _ in range(T):
    n = int(input())
    print(sum(dp[n-1]) % MOD)


"""
import sys


def solution():
    repeat  = int(sys.stdin.readline())

    unit    = 1000000009
    LUT_DP  = [[0]*4 for _ in range(100000+1)]
    # 인덱스와 숫자(값)를 맞춤
    LUT_DP[1] = [0,1,0,0]
    LUT_DP[2] = [0,0,1,0]
    LUT_DP[3] = [0,1,1,1]

    for i in range(4, 100000+1):
        LUT_DP[i][1] = (LUT_DP[i-1][2] + LUT_DP[i-1][3]) % unit
        LUT_DP[i][2] = (LUT_DP[i-2][1] + LUT_DP[i-2][3]) % unit
        LUT_DP[i][3] = (LUT_DP[i-3][1] + LUT_DP[i-3][2]) % unit
    
    for _ in range(repeat):
        print(sum(LUT_DP[int(sys.stdin.readline())]) % unit)


solution()
"""