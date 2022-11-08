from _collections import deque


def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    limit = len(queue1)
    total = sum1 + sum2
    diff = sum1 - sum2

    if total % 2 != 0:
        return -1

    while True:
        # print("queue1 : ")
        # for e in queue1:
        #     print(e, end=' ')
        # print()
        # print("queue2 : ")
        # for e in queue2:
        #     print(e, end=' ')
        # print("\n")

        if diff == 0:
            if sum(queue1) == total / 2:
                break
            else:
                answer = -1
                break
        elif diff < 0:
            if len(queue2) <= 1:
                answer = -1
                break
            pop = queue2.popleft()
            queue1.append(pop)
            diff += pop * 2
            answer += 1
        else:
            if len(queue1) <= 1:
                answer = -1
                break
            pop = queue1.popleft()
            queue2.append(pop)
            diff -= pop * 2
            answer += 1
        if answer == limit * 4:
            answer = -1
            break
    # print(answer)
    return answer

solution([3, 2, 7, 2]		, [4, 6, 5, 1]	)
