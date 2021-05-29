import heapq
import sys

n = int(sys.stdin.readline().rstrip())
numbers = []
lst = list(map(int, sys.stdin.readline().rstrip().split()))
for i in lst:
    heapq.heappush(numbers, i)
for _ in range(n - 1):
    lst = list(map(int, sys.stdin.readline().rstrip().split()))
    for num in lst:
        if num > numbers[0]:
            heapq.heappush(numbers, num)
            heapq.heappop(numbers)
print(numbers[0])