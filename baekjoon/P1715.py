import heapq
n=int(input())
heap=[]
result=0
for _ in range(n):
    heapq.heappush(heap,int(input()))
while len(heap)>=2:
    a=heapq.heappop(heap)
    b=heapq.heappop(heap)
    prev=a+b
    result+=prev
    heapq.heappush(heap, prev)
print(result)