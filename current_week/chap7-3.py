import  sys
input = sys.stdin.readline

def binary_search(start, end):
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        total_length = 0
        for cake in rice_cakes:
            if mid < cake:
                total_length += (cake - mid)
        if total_length == m:
            return mid
        elif total_length > m:
            start = mid + 1
            ans = max(ans, mid)
        else:
            end = mid - 1
            ans = max(ans, mid)
    return ans

n,m = map(int, input().split())
rice_cakes = list(map(int, input().split()))
rice_cakes.sort()
print(binary_search(0, max(rice_cakes)))
