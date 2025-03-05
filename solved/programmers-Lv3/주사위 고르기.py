def solution(dice):
    n = len(dice)

    max_wins = 0
    result = []
    
    combinations = half_combination(n, 0, [], 0, [])
    for combination in combinations:
        opposite = []
        for idx in range(n):
            if idx not in combination:
                opposite.append(idx)
                
        a_statistic = sum_statistics(dice, combination)
        b_statistic = sum_statistics(dice, opposite)
        
        num = num_of_first_wins(a_statistic, b_statistic)
        
        if max_wins < num:
            max_wins = num
            result = combination
    return [i + 1 for i in result]


def num_of_first_wins(a, b):
    wins = 0
    for k1, v1 in a.items():
        for k2, v2 in b.items():
            if k1 > k2:
                wins += v1 * v2
    return wins


def half_combination(n, length, comb, start, result):
    if length == n//2:
        result.append([e for e in comb])
        return
    
    for i in range(start, n):
        comb.append(i)
        half_combination(n, length + 1, comb, i + 1, result)
        comb.pop(-1)
        
    return result


def sum_statistics(dice, combination):
    result = dict()
    for num in dice[combination[0]]:
        result[num] = result.get(num, 0) + 1
    
    
    for i in combination[1:]:
        next = dict()
        for num in dice[i]:
            for k, v in result.items():
                next[k + num] = next.get(k+num, 0) + v
        result = next
    return result