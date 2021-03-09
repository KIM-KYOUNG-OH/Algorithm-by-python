import heapq

def solution(operations):
    lst = []
    answer = []
    for i in range(len(operations)):
        if operations[i] == "D -1":
            if lst:
                heapq.heappop(lst)
        elif operations[i] == "D 1":
            if lst:
                lst.remove(max(lst))
        else:
            temp = list(operations[i].split(" "))
            heapq.heappush(lst, int(temp[1]))
    if len(lst) == 0:
        return [0,0]
    answer.append(max(lst))
    answer.append(heapq.heappop(lst))
    return answer

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))