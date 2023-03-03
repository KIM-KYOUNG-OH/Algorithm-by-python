from collections import Counter, deque


def solution(k, tangerine):
    kind = set(tangerine)
    answer = len(kind)
    mc = deque(Counter(tangerine).most_common())
    move_cnt = len(tangerine) - k
    while move_cnt > 0:
        size, cnt = mc.pop()
        if cnt > move_cnt:
            break
        else:
            move_cnt -= cnt
            answer -= 1
    return answer

