from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    q = deque([0] * bridge_length)
    time = 0
    cur_weight = 0
    while True:
        time += 1
        out = q.popleft()
        cur_weight -= out
        new = 0
        if truck_weights[0] + cur_weight <= weight:
            new = truck_weights[0]
            truck_weights.popleft()
        q.append(new)
        cur_weight += new

        print('time = ', time)

        print('q = ', q)
        if len(truck_weights) == 0:
            break
    time += bridge_length
    return time


print(solution(2, 10, [7,4,5,6]))
# print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
