from collections import deque


def solution(bridge_length, weight, truck_weights):  # 다리가 견딜 수 있는 최대 트럭수, 최대 무게, 트럭 무게 리스트
    crossing = [0] * bridge_length  # 다리를 건너는 트럭
    waiting = deque(truck_weights)  # 대기중인 트럭
    time = 0  # 현재 시간
    while crossing:
        time += 1
        crossing.pop(0)
        if waiting:
            if sum(crossing) + waiting[0] <= weight:
                crossing.append(waiting.popleft())
            else:
                crossing.append(0)

    return time


print(solution(2,10,[7,4,5,6]))