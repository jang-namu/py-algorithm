def solution(price, money, count):
    accumulated_count = count * (count + 1) / 2
    accumulated_price = accumulated_count * price
    answer = accumulated_price - money if accumulated_price > money else 0

    return answer