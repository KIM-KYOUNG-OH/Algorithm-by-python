def solution(id_list, report, k):
    answer = []
    banned_cnt_dic = dict()
    answer_cnt_dic = dict()
    for id in id_list:
        banned_cnt_dic[id] = 0
        answer_cnt_dic[id] = 0
    report = list(set(report))
    for rep in report:
        frm, to = rep.split(' ')
        banned_cnt_dic[to] += 1
    for rep in report:
        frm, to = rep.split(' ')
        if banned_cnt_dic[to] >= k:
            answer_cnt_dic[frm] += 1
    for id in id_list:
        answer.append(answer_cnt_dic[id])
    return answer