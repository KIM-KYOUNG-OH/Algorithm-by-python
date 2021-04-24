def binary_search(start, end):
    ans = 0
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for tree in trees:
            if tree > mid:
                total += tree - mid
        if total >= m:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
    return ans


n, m = map(int, input().split())
trees = list(map(int, input().split()))
print(binary_search(0, max(trees)))