from collections import deque


def bfs(n, info):
    res = []
    q = deque([(0, [0 for _ in range(11)])])
    max_diff = 0

    while q:
        focus, arrow = q.popleft()

        if sum(arrow) == n:
            diff = calc(arrow, info)
            if diff > 0:
                if max_diff > diff:
                    continue
                elif max_diff < diff:
                    max_diff = diff
                    res.clear()
                res.append(arrow)
        elif sum(arrow) > n:
            continue
        elif focus == 10:
            tmp = arrow.copy()
            tmp[focus] = n - sum(tmp)
            q.append((-1, tmp))
        else:
            tmp = arrow.copy()
            tmp[focus] = info[focus] + 1
            q.append((focus + 1, tmp))
            tmp2 = arrow.copy()
            tmp2[focus] = 0
            q.append((focus + 1, tmp2))
    return res


def calc(lion, apeach):
    apeach_score = 0
    lion_score = 0
    for i in range(11):
        if apeach[i] == 0 and lion[i] == 0:
            continue
        elif apeach[i] >= lion[i]:
            apeach_score += 10 - i
        else:
            lion_score += 10 - i
    return lion_score - apeach_score


def solution(n, info):
    win_list = bfs(n, info)

    if not win_list:
        return [-1]
    elif len(win_list) == 1:
        return win_list[0]
    else:
        return win_list[-1]

solution(9, [0,0,1,2,0,1,1,1,1,1,1])