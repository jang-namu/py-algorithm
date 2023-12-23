def solution(nums):
    not_duplicated = set(nums)
    return min(len(nums)/2, len(not_duplicated))