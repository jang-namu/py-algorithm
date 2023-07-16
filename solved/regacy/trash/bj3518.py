# 3518 공백왕 빈-칸
import sys
input = sys.stdin.readline

paragraph = sys.stdin.readlines()
max_length = [0] * 180
arrs = []

for sentence in paragraph:
    arrs.append(sentence.split())
    for idx, s in enumerate(arrs[-1]):
        max_length[idx] = max(max_length[idx], len(s))

for arr in arrs:
    for idx, word in enumerate(arr[:-1]):
        print(word + " " * (max_length[idx] - len(word)+1), end="")
    print(arr[-1])
