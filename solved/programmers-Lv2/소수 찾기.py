from itertools import permutations

prime_numbers = [True] * 10000000
prime_numbers[0] = False
prime_numbers[1] = False

for i in range(2, 3164):
    if not prime_numbers[i]:
        continue
    for j in range(2*i, 10000000, i):
        prime_numbers[j] = False


def solution(numbers):
    answer = 0
    atomic_nums = set()

    length = len(numbers)
    for i in range(1, length + 1):
        for k in permutations(numbers, i):  # list() 하나만 뺐는데 엄청 빨라졌다!
            atomic_nums.add(int("".join(k)))

    for nums in atomic_nums:
        if prime_numbers[nums]:
            answer += 1
    return answer

