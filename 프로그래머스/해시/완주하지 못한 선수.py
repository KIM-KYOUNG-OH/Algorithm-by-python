# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#     for i in range(len(completion)):
#         if completion[i] != participant[i]: # 순서가 다른 순간 i번째가 답
#             return participant[i]
#     return participant[-1] # 전부 일치하면 마지막에 남은애가 답


def solution(participant, completion):
    answer = ''
    completion_dic = dict()  # 해시
    for i in completion:
        if i in completion_dic:  # 이름이 중복되서 나오면 value +1
            completion_dic[i] += 1
            continue
        completion_dic[i] = 1  # 처음 나온 선수면 해시에 추가
    while participant:
        select = participant.pop()  # 참가자중 한명 뽑기
        if select not in completion_dic:  # 해시에 없으면 완주 못한 사람이므로 출력후 함수 종료
            answer = select
            break
        completion_dic[select] -= 1  # 해시에 있으면 value -1
        if completion_dic[select] == 0:  # value가 0이 되면 해시에서 삭제
            del completion_dic[select]
    return answer


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))