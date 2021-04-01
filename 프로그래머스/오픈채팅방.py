def solution(record) -> int:
    answer = []
    events = []
    dic = dict()
    for order in record:
        lst = order.split(' ')
        if lst[0] == "Enter":
            events.append((lst[1], "님이 들어왔습니다."))
            dic[lst[1]] = lst[2]
        elif lst[0] == "Leave":
            events.append((lst[1], "님이 나갔습니다."))
        elif lst[0] == "Change":
            dic[lst[1]] = lst[2]
    for a in events:
        answer.append("".join([dic[a[0]], a[1]]))

    return answer


print(solution(
    ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))

