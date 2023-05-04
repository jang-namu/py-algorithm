# 9342 염색체

import sys
input = sys.stdin.readline

key_start = ('B', 'C', 'D', 'E', 'F')
key_end = ('A', 'B', 'D', 'E', 'F')

T = int(input())
for _ in range(T):
    bio = input().rstrip()
    verify = [bio[0]]
    idx = 0
    for ch in bio[1:]:
        if ch == verify[idx]:
            continue
        verify.append(ch)
        idx += 1

    ans = "Good"
    if verify[0] == 'A':
        if len(verify) == 3 and verify[1] == 'F' and verify[2] == 'C':
            ans = "Infected!"
        if len(verify) == 4 and verify[1] == 'F' and verify[2] == 'C' and verify[-1] in key_end:
            ans = "Infected!"
    elif verify[0] in key_start:
        if len(verify) == 4 and verify[1] == 'A' and verify[2] == 'F' and verify[3] == 'C':
            ans = "Infected!"
        if len(verify) == 5 and verify[1] == 'A' and verify[2] == 'F' and verify[3] == 'C' and verify[-1] in key_end:
            ans = "Infected!"
    print(ans)