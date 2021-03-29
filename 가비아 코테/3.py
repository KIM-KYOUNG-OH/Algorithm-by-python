from collections import deque

def solution(N:int, coffee_times:list) -> list:
    answer = []
    q = deque([i for i in range(1, len(coffee_times)+1)])
    enter_time = dict()
    second = 0
    making = [i for i in range(1, N+1)]
    for i in making:
        enter_time[i] = 0
        q.popleft()
    while making:
        second += 1
        temp = []
        for i in range(len(making)):
            if second-enter_time[making[i]] == coffee_times[making[i]-1]:
                answer.append(making[i])
                temp.append(making[i])
        for i in temp:
            making.remove(i)
        for _ in range(N-len(making)):
            if len(making)<N and q:
                num = q.popleft()
                making.append(num)
                enter_time[num] = second

    return answer

print(solution(3, [4, 2, 2, 5, 3]))