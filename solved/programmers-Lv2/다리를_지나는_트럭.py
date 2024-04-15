from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    w = 0
    time = 0

    while bridge:
        time += 1
        w -= bridge.popleft()
        if truck_weights:
            if w + truck_weights[0] <= weight:
                w += truck_weights[0]
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)

    return time


