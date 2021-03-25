import heapq

def solution(arr):
    while len(arr)>1:
        a,b = heapq.heappop(arr), heapq.heappop(arr)
        i  = 1
        while True:
            mul = b*i
            if mul%a == 0:
                heapq.heappush(arr, mul)
                break
            i += 1

    return arr[0]