# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#     for i in range(len(completion)):
#         if completion[i] != participant[i]: # 순서가 다른 순간 i번째가 답
#             return participant[i]
#     return participant[-1] # 전부 일치하면 마지막에 남은애가 답


def solution(participant, completion):
    answer = ''
    completion_dic = dict()
    for i in completion:
        if i in completion_dic:
            completion_dic[i] += 1
            continue
        completion_dic[i] = 1
    while participant:
        select = participant.pop()
        if select not in completion_dic:
            answer = select
            break
        completion_dic[select] -= 1
        if completion_dic[select] == 0:
            del completion_dic[select]
    return answer  


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))