import heapq


def solution(n, works):
    pq = []
    for work in works:
        heapq.heappush(pq, -1 * work)

    while n > 0:
        if len(pq) == 0:
            break
        n -= 1
        cur = heapq.heappop(pq)
        cur = -1 * (abs(cur) - 1)
        if cur == 0:
            continue
        heapq.heappush(pq, cur)

    answer = 0
    for e in pq:
        answer += e ** 2
    return answer


print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(3, [1, 1]))
