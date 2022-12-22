import heapq


def solution(operations):
    min_heap = []
    max_heap = []
    for oper in operations:
        op, n = oper.split(' ')
        if op == 'I':
            heapq.heappush(min_heap, (int(n)))
            heapq.heappush(max_heap, (int(n) * -1))
        else:
            if not min_heap:
                continue
            elif n == '-1':
                cur = heapq.heappop(min_heap)
                max_heap.remove(cur * -1)
            elif n == '1':
                cur = heapq.heappop(max_heap)
                min_heap.remove(cur * -1)
    if not min_heap:
        return [0, 0]
    else:
        return [heapq.heappop(max_heap) * -1, heapq.heappop(min_heap)]


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
