def solution(records):
    answer = []
    name = dict()
    messages = []
    for record in records:
        arr = record.split(' ')
        if arr[0] == 'Enter':
            name[arr[1]] = arr[2]
            messages.append((arr[0], arr[1]))
        elif arr[0] == 'Leave':
            messages.append((arr[0], arr[1]))
        else:
            name[arr[1]] = arr[2]

    for message in messages:
        order, id = message
        if order == 'Enter':
            answer.append('{}님이 들어왔습니다.'.format(name[id]))
        else:
            answer.append('{}님이 나갔습니다.'.format(name[id]))
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))