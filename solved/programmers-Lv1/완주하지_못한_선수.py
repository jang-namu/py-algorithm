# 해시값 이용, 딕셔너리는 해시값:이름 쌍 저장
def solution(participant, completion):
    people = dict()
    tracked_value = 0

    for person in participant:
        hashed_value = hash(person)
        people[hashed_value] = person
        tracked_value += hashed_value

    for person in completion:
        tracked_value -= hash(person)

    return people[tracked_value]


# Counter간 뺄셈
"""
from collections import Counter

def solution(participant, completion):
    participant_dict = Counter(participant)
    completion_dict = Counter(completion)

    return list(participant_dict - completion_dict)[0]
"""

# 내 정답
"""
def solution(participant, completion):
    participant_and_completion = dict()

    for name in participant:
        participant_and_completion[name] = participant_and_completion.get(name, 0) + 1

    for name in completion:
        if participant_and_completion[name] == 1:
            del participant_and_completion[name]
            continue
        participant_and_completion[name] -= 1

    answer = str(*participant_and_completion.keys())
    return answer

"""