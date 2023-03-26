# 2805 나무 자르기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = list(map(int, input().split()))
tree.sort()

if M == 0:
    print(0)
    exit()

ans = -1
start = 0
end = N-1
wood = 0
while start != end:
    mid = int((start + end) / 2 + 0.5)
    wood = sum(tree[mid+1:]) - tree[mid] * (N-mid-1)
    if wood > M:
        start = mid + 1
        continue
    elif wood < M:
        end = mid
        continue
    else:
        ans = tree[mid]
        break

if ans == -1:
    ans = tree[mid] + (wood - M) // (N-mid-1)

print(ans)



