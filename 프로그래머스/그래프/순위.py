def solution(n, results):
    answer = 0
    lower = [set() for _ in range(n+1)]
    upper = [set() for _ in range(n+1)]

    for [winner, loser] in results:
        upper[loser].add(winner)
        lower[winner].add(loser)

    for i in range(1, n+1):
        for low in lower[i]:
            upper[low].update(upper[i])
        for up in upper[i]:
            lower[up].update(lower[i])

    for i in range(1, n+1):
        if len(upper[i]) + len(lower[i]) == n - 1:
            answer += 1

    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))