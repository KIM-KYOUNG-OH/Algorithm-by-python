def solution(n, k, cmd):
    answer = ''
    deleted = []  # stack
    rows = dict()
    for i in range(n):
        rows[i] = 1  # 행이 존재하면 1 아니면 0
    current = k  # 현재 위치
    for order in cmd:
        order = order.split()
        if order[0] == 'D':
            cnt = 0
            for j in deleted:
                if current <= j < current + int(order[1]) and rows[j] == 0:
                    cnt += 1
            current += int(order[1]) + cnt
            continue
        if order[0] == 'U':
            cnt = 0
            for j in deleted:
                if current - int(order[1]) <= j < current and rows[j] == 0:
                    cnt += 1
            current -= int(order[1]) + cnt
            continue
        if order[0] == 'C':
            deleted.append(current)
            rows[current] = 0
            if current == n - 1:  # 마지막 행에서 삭제시
                while True:
                    current -= 1
                    if rows[current] == 1:
                        break
                continue
            while True:
                current += 1
                if rows[current] == 1:
                    break
        if order[0] == 'Z':
            recover = deleted.pop()
            rows[recover] = 1
    result = sorted(list(rows.items()), key=lambda x: x[0])
    for i in result:
        if i[1] == 0:
            answer += 'X'
            continue
        if i[1] == 1:
            answer += 'O'
            continue

    return answer


print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))