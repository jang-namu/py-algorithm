# 9536 여우는 어떻게 울지?
"""
    a, *b, c 로 입력 받을 때, 중간에도 여러 항목을 받을 수 있다.
"""
t = int(input())
for _ in range(t):
  sound = input().split()
  cry = set()
  while True:
    a, *b, c = input().split()  # 중간에 배열이 들어갈 수 있다.
    print(b)
    if a == 'what':
      break
    cry.add(c)
  ans = [s for s in sound if s not in cry]
  print(*ans, sep=' ')