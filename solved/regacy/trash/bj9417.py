# 9417 최대 GCD
def gcd(a, b):
  if b==0:
    return a
  return gcd(b, a%b)


n = int(input())
mins = []
for idx in range(n):
  nums = list(map(int, input().split()))
  mins.append(0)
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      if mins[idx] < gcd(nums[i], nums[j]):
        mins[idx] = gcd(nums[i], nums[j])
print('\n'.join(map(str, mins)))