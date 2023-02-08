def solution(n, stations, w):
    length = 2 * w + 1
    start = 1
    answer = 0
    for station in stations:
        end = station - w - 1
        if start <= end:
            cnt = (end - start + 1 + 2 * w) // length
            answer += cnt
        start = station + w + 1
    if start <= n:
        cnt = (n - start + 1 + 2 * w) // length
        answer += cnt
    return answer


print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))
# print(solution(200000000, [4, 11], 1))
