def solution(citations):
    citations.sort(reverse=True)
    n = len(citations)
    for ans in range(n, -1, -1):
        cnt = 0
        for i in range(n):
            if citations[i] >= ans:
                cnt += 1
            else:
                break
        rest = n - cnt
        if cnt >= ans >= rest:
            return ans


print(solution([3, 0, 6, 1, 5]))
print(solution([10, 100]))