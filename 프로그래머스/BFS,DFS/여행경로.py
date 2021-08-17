def solution(tickets):
    path_dic = dict()
    for ticket in tickets:
        frm, to = ticket
        if frm not in path_dic:
            path_dic[frm] = [to]
            continue
        path_dic[frm].append(to)
    for key in path_dic.keys():
        path_dic[key].sort(reverse=True)

    answer = []
    stack = ['ICN']
    while stack:
        top = stack[-1]
        if top not in path_dic or not path_dic[top]:
            answer.append(stack.pop())
        else:
            stack.append(path_dic[top].pop())
    return answer[::-1]


print(solution([["ICN", "BOO"], ["ICN", "COO"], ["COO", "ICN"]]))