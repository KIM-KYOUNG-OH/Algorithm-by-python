def solution(name):
    answer = 0
    n = len(name)
    min_move = n - 1

    for i, ch in enumerate(name):
        answer += min(ord(ch) - ord('A'), ord('Z') - ord(ch) + 1)

        next = i + 1
        while next < n and name[next] == 'A':
            next += 1

        min_move = min([min_move, i * 2 + n - next, (n - next) * 2 + i])

    answer += min_move
    return answer